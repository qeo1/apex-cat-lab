const questions = {
  QUANT: {
    key: 'quant-ratio-sample-v1', label: 'QUANT · RATIO MODEL',
    prompt: 'Two pumps fill a tank at rates in the ratio 3 : 5. Working together, they fill the tank in 4 hours. How long would the faster pump take working alone?',
    choices: ['5 hours', '6.4 hours', '8 hours', '10 hours'], answer: 1,
    hint: 'Treat the rates as 3k and 5k. Their combined rate fills one tank in 4 hours.',
    explain: 'Together the pumps work at 1/4 tank per hour. The faster pump contributes 5/8 of the combined rate: (5/8) × (1/4) = 5/32 tank per hour. Its solo time is the reciprocal, 32/5 = 6.4 hours.'
  },
  DILR: {
    key: 'dilr-order-sample-v1', label: 'DILR · CONSTRAINTS',
    prompt: 'Four talks P, Q, R and S are scheduled in four consecutive slots. P is before R. Q is immediately after S. Which sequence is possible?',
    choices: ['P, S, Q, R', 'S, Q, R, P', 'R, P, S, Q', 'S, P, Q, R'], answer: 0,
    hint: 'Keep S–Q together as a block. Then check whether P still comes before R.',
    explain: 'The pair S–Q must occupy adjacent slots in that order. P must appear before R. In P, S, Q, R both conditions hold. The other options either put R before P or split the required pair.'
  },
  VARC: {
    key: 'varc-inference-sample-v1', label: 'VARC · INFERENCE',
    prompt: 'A city expands its cycle lanes, and bicycle trips rise by 18%. During the same period, public transit fares increase and a major road closes for repairs. Which conclusion is best supported?',
    choices: ['Cycle lanes alone caused the full increase.', 'The increase proves most new cyclists were commuters.', 'Bicycle trips rose, but the effect of the lanes cannot be isolated from these facts.', 'The road closure had no effect on travel choices.'], answer: 2,
    hint: 'Separate the observed change from a claim about its cause.',
    explain: 'The rise in bicycle trips is observed. But fare changes and a road closure also changed travel conditions, so these facts cannot identify the independent effect of cycle lanes.'
  }
};

const SUPABASE_URL = 'https://adlgchkwmwvoxeaohlhz.supabase.co';
const SUPABASE_KEY = 'sb_publishable_qQ0jIYNp6nkX-Auxg7LN0w_rpLN05tq';
const read = () => { try { return JSON.parse(localStorage.getItem('apex-progress') || '{}'); } catch { return {}; } };
const makeId = () => crypto.randomUUID();
let state = read();
let selected = null, current = 'QUANT', answered = false, session = null, syncInFlight = null, syncTimer = null;
state.events = Array.isArray(state.events) ? state.events : [];

const indiaDate = (value = new Date()) => new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Kolkata' }).format(value);
const indiaDateTime = (date) => new Date(`${date}T12:00:00+05:30`).toISOString();
const persist = () => localStorage.setItem('apex-progress', JSON.stringify(state));

// Preserve earlier browser-only totals when the event history is first introduced.
if (!state.legacyEventsAdded) {
  const missing = Math.max(0, Number(state.attempts || 0) - state.events.length);
  const priorCorrect = Math.max(0, Number(state.correct || 0) - state.events.filter(e => e.is_correct).length);
  const practiceDate = state.lastPracticeDate || indiaDate();
  for (let i = 0; i < missing; i++) {
    state.events.push({
      event_id: makeId(), question_key: 'legacy-local-practice', section: 'UNKNOWN',
      is_correct: i < priorCorrect, occurred_at: indiaDateTime(practiceDate)
    });
  }
  state.legacyBest = Number(state.best || 0);
  state.legacyStreak = Number(state.streak || 0);
  state.legacyLastPracticeDate = state.lastPracticeDate || null;
  state.legacyEventsAdded = true;
}

const dateFromEvent = event => indiaDate(new Date(event.occurred_at));
const calculateStreaks = events => {
  const dates = [...new Set(events.map(dateFromEvent))].sort();
  let best = 0, run = 0, previous = null;
  for (const day of dates) {
    const previousDay = previous ? new Date(`${previous}T12:00:00+05:30`) : null;
    const thisDay = new Date(`${day}T12:00:00+05:30`);
    run = previousDay && thisDay - previousDay === 86400000 ? run + 1 : 1;
    best = Math.max(best, run);
    previous = day;
  }
  const today = indiaDate();
  const yesterdayDate = new Date(); yesterdayDate.setDate(yesterdayDate.getDate() - 1);
  const yesterday = indiaDate(yesterdayDate);
  const latest = dates.at(-1) || null;
  const currentRun = latest === today || latest === yesterday ? run : 0;
  return { best, current: currentRun, latest };
};

const recompute = () => {
  state.attempts = state.events.length;
  state.correct = state.events.filter(e => e.is_correct).length;
  const run = calculateStreaks(state.events);
  state.streak = Math.max(run.current, state.legacyLastPracticeDate === run.latest ? state.legacyStreak : 0);
  state.best = Math.max(Number(state.legacyBest || 0), run.best, state.streak);
  state.lastPracticeDate = run.latest;
};

const paint = () => {
  document.querySelector('#total-solved').textContent = state.attempts || 0;
  document.querySelector('#accuracy').innerHTML = `${state.attempts ? Math.round(state.correct / state.attempts * 100) : '—'}<i>%</i>`;
  document.querySelector('#streak').textContent = state.streak || 0;
  document.querySelector('#best-streak').innerHTML = `${state.best || 0}<i>d</i>`;
  document.querySelector('#progress-fill').style.width = `${Math.min((state.attempts || 0) / 12 * 100, 100)}%`;
  document.querySelector('#foundation-progress').textContent = `${Math.min(state.attempts || 0, 12)} / 12 concepts`;
  const days = Math.max(0, Math.ceil((new Date('2026-11-29T00:00:00+05:30') - new Date()) / 864e5));
  document.querySelector('#days-left').textContent = days;
};

const showSync = (title, detail, status = '') => {
  document.querySelector('#sync-title').textContent = title;
  document.querySelector('#sync-detail').textContent = detail;
  document.querySelector('#sync-dot').className = `sync-dot ${status}`;
};
const showAccount = () => {
  const signedOut = document.querySelector('#account-signed-out');
  const signedIn = document.querySelector('#account-signed-in');
  signedOut.hidden = !!session;
  signedIn.hidden = !session;
  document.querySelector('#account-button').textContent = session ? 'Account' : 'Sign in';
  document.querySelector('#account-email-label').textContent = session?.user?.email || '';
};

let supabase = null;

const fetchAllEvents = async () => {
  const rows = [];
  for (let offset = 0; ; offset += 1000) {
    const { data, error } = await supabase.from('practice_events')
      .select('event_id,user_id,question_key,section,is_correct,occurred_at')
      .order('occurred_at', { ascending: true }).range(offset, offset + 999);
    if (error) throw error;
    rows.push(...(data || []));
    if (!data || data.length < 1000) break;
  }
  return rows;
};

const syncCloud = () => {
  if (syncInFlight) return syncInFlight;
  if (!supabase || !session) return Promise.resolve();
  syncInFlight = (async () => {
    showSync('Syncing progress', 'Connecting to your account…', 'sync-pending');
    const userId = session.user.id;
    const remote = await fetchAllEvents();
    const remoteIds = new Set(remote.map(e => e.event_id));
    const missing = state.events.filter(e => !remoteIds.has(e.event_id)).map(e => ({
      event_id: e.event_id, user_id: userId, question_key: e.question_key,
      section: e.section, is_correct: e.is_correct, occurred_at: e.occurred_at
    }));
    if (missing.length) {
      const { error } = await supabase.from('practice_events').upsert(missing, { onConflict: 'user_id,event_id' });
      if (error) throw error;
    }
    const all = await fetchAllEvents();
    const merged = new Map(state.events.map(e => [e.event_id, e]));
    all.forEach(e => merged.set(e.event_id, e));
    state.events = [...merged.values()].sort((a, b) => a.occurred_at.localeCompare(b.occurred_at));
    recompute(); persist(); paint();
    showSync('Progress synced', `Saved to ${session.user.email}`, 'sync-ok');
  })().catch(error => {
    console.error('Progress sync failed', error);
    showSync('Saved on this device', 'Cloud sync will retry when available', 'sync-error');
    const message = document.querySelector('#signed-in-message');
    if (message && !document.querySelector('#account-dialog').open) return;
    if (message) { message.textContent = 'Your local progress is safe; syncing can be retried later.'; message.classList.add('error'); }
  }).finally(() => { syncInFlight = null; });
  return syncInFlight;
};

const scheduleSync = () => {
  if (!session || !supabase) return;
  showSync('Progress waiting to sync', 'Saved locally while connecting…', 'sync-pending');
  clearTimeout(syncTimer);
  syncTimer = setTimeout(() => syncCloud(), 300);
};

const openQuiz = (section = 'QUANT') => {
  current = section; selected = null; answered = false;
  const q = questions[section];
  document.querySelector('#quiz-section').textContent = q.label;
  document.querySelector('#question-text').textContent = q.prompt;
  document.querySelector('#feedback').textContent = '';
  document.querySelector('#options').innerHTML = q.choices.map((choice, i) => `<button class="option" data-index="${i}"><span class="choice-letter">${'ABCD'[i]}.</span> ${choice}</button>`).join('');
  document.querySelectorAll('.option').forEach(button => button.onclick = () => {
    if (answered) return;
    selected = +button.dataset.index;
    document.querySelectorAll('.option').forEach(option => option.classList.toggle('selected', option === button));
  });
  document.querySelector('#quiz-dialog').showModal();
};

document.querySelector('#start-session').onclick = () => openQuiz(['QUANT', 'DILR', 'VARC'][Math.floor(Math.random() * 3)]);
document.querySelectorAll('[data-section]').forEach(link => link.onclick = () => openQuiz(link.dataset.section));
document.querySelector('.close-quiz').onclick = () => document.querySelector('#quiz-dialog').close();
document.querySelector('#quiz-dialog').onclick = event => { if (event.target === event.currentTarget) event.currentTarget.close(); };
document.querySelector('#hint-button').onclick = () => { document.querySelector('#feedback').textContent = `Hint: ${questions[current].hint}`; };
document.querySelector('#submit-answer').onclick = () => {
  if (answered) { document.querySelector('#quiz-dialog').close(); return; }
  if (selected === null) { document.querySelector('#feedback').textContent = 'Choose an answer to check your reasoning.'; return; }
  answered = true;
  const question = questions[current], good = selected === question.answer;
  const event = {
    event_id: makeId(), question_key: question.key, section: current,
    is_correct: good, occurred_at: new Date().toISOString()
  };
  state.events.push(event);
  recompute(); persist(); paint(); scheduleSync();
  document.querySelectorAll('.option').forEach((button, i) => {
    if (i === question.answer) button.classList.add('correct');
    if (i === selected && !good) button.classList.add('wrong');
  });
  document.querySelector('#feedback').innerHTML = `<strong>${good ? 'Good reasoning.' : 'Revisit the setup.'}</strong> ${question.explain}`;
  document.querySelector('#submit-answer').innerHTML = 'Done <span>✓</span>';
};

document.querySelector('#account-button').onclick = () => {
  showAccount();
  document.querySelector('#auth-message').textContent = '';
  document.querySelector('#signed-in-message').textContent = '';
  document.querySelector('#account-dialog').showModal();
};
document.querySelector('.close-account').onclick = () => document.querySelector('#account-dialog').close();
document.querySelector('#account-dialog').onclick = event => { if (event.target === event.currentTarget) event.currentTarget.close(); };
const authMessage = (text, error = false) => {
  const message = document.querySelector('#auth-message');
  message.textContent = text;
  message.classList.toggle('error', error);
};
document.querySelector('#sign-in-button').onclick = async () => {
  if (!supabase) return authMessage('Account service is still loading. Please try again in a moment.', true);
  const email = document.querySelector('#account-email').value.trim();
  const password = document.querySelector('#account-password').value;
  if (!email || !password) return authMessage('Enter your email and password.', true);
  const { data, error } = await supabase.auth.signInWithPassword({ email, password });
  if (error) return authMessage(error.message, true);
  session = data.session; showAccount(); syncCloud();
};
document.querySelector('#sign-up-button').onclick = async () => {
  if (!supabase) return authMessage('Account service is still loading. Please try again in a moment.', true);
  const email = document.querySelector('#account-email').value.trim();
  const password = document.querySelector('#account-password').value;
  if (!email || !password) return authMessage('Enter your email and a password with at least 8 characters.', true);
  const { data, error } = await supabase.auth.signUp({
    email, password, options: { emailRedirectTo: `${window.location.origin}/` }
  });
  if (error) return authMessage(error.message, true);
  if (data.session) { session = data.session; showAccount(); syncCloud(); }
  else authMessage('Check your email to confirm your account, then sign in here.');
};
document.querySelector('#sign-out-button').onclick = async () => {
  const { error } = await supabase.auth.signOut();
  if (error) { document.querySelector('#signed-in-message').textContent = error.message; return; }
  session = null; showAccount(); showSync('Saved on this device', 'Sign in to sync across devices');
};

const initializeBackend = async () => {
  showSync('Loading account service', 'Local practice is ready', 'sync-pending');
  try {
    if (!window.supabase?.createClient) {
      await new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.118.0/dist/umd/supabase.min.js';
        script.async = true;
        script.onload = resolve;
        script.onerror = () => reject(new Error('Supabase client could not be loaded'));
        document.head.appendChild(script);
      });
    }
    if (!window.supabase?.createClient) throw new Error('Supabase client did not initialize');
    supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
    supabase.auth.onAuthStateChange((_event, nextSession) => {
      session = nextSession; showAccount();
      if (session) setTimeout(() => syncCloud(), 0);
      else showSync('Saved on this device', 'Sign in to sync across devices');
    });
    const { data, error } = await supabase.auth.getSession();
    if (error) throw error;
    session = data.session; showAccount();
    if (session) await syncCloud();
    else showSync('Saved on this device', 'Sign in to sync across devices');
  } catch (error) {
    console.error('Account service failed to load', error);
    showSync('Saved on this device', 'Account service could not load', 'sync-error');
  }
};

recompute(); persist(); paint(); showAccount();
initializeBackend();
if ('serviceWorker' in navigator) navigator.serviceWorker.register('./sw.js').catch(() => {});

