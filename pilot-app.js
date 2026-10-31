const escapeHTML = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
let pilot = null, pilotFilter = 'ALL';

const renderPilot = () => {
  const host = document.querySelector('#pilot-content');
  if (!pilot) return;
  host.replaceChildren();
  const questionsToShow = pilot.questions.filter(q => pilotFilter === 'ALL' || q.section === pilotFilter);
  const shownGroups = new Set();
  questionsToShow.forEach(q => {
    if (q.group_id && !shownGroups.has(q.group_id)) {
      const group = pilot.groups.find(item => item.id === q.group_id);
      shownGroups.add(q.group_id);
      const groupEl = document.createElement('article');
      groupEl.className = 'pilot-group';
      groupEl.innerHTML = `<h3>${escapeHTML(group.title)}</h3><p>${escapeHTML(group.context)}</p>`;
      host.append(groupEl);
    }
    const benchmark = pilot.benchmarks[q.benchmark_id];
    const source = pilot.sources[q.research_id];
    const card = document.createElement('article');
    card.className = 'pilot-card';
    card.dataset.pilotId = q.id;
    card.dataset.answerState = 'open';
    card.innerHTML = `
      <div class="pilot-card-top"><span class="pilot-card-meta">${escapeHTML(q.id)} · ${escapeHTML(q.section)} · ORIGINAL PRACTICE</span><span class="pilot-badge">RESEARCH PILOT</span></div>
      <h3>${escapeHTML(q.prompt)}</h3>
      <div class="pilot-options" role="radiogroup" aria-label="Answer choices for ${escapeHTML(q.id)}">
        ${q.choices.map((choice,i)=>`<label class="pilot-option"><input type="radio" name="${escapeHTML(q.id)}" value="${i}"><span><b>${'ABCD'[i]}.</b> ${escapeHTML(choice)}</span></label>`).join('')}
      </div>
      <div class="pilot-hint" hidden aria-live="polite"></div><div class="pilot-result" hidden aria-live="polite"></div>
      <div class="pilot-actions"><button class="quiet-button pilot-hint-button" type="button">Show hint 1 of ${q.hints.length}</button><button class="button button-dark pilot-check" type="button">Check answer</button></div>
      <details class="pilot-provenance"><summary>Research, benchmark, solutions and difficulty</summary><dl>
        <dt>CAT benchmark</dt><dd>${escapeHTML(benchmark.label)} <a href="${escapeHTML(benchmark.url)}" target="_blank" rel="noopener">Open source ↗</a><br>${escapeHTML(benchmark.fingerprint)}</dd>
        <dt>Research source</dt><dd><a href="${escapeHTML(source.url)}" target="_blank" rel="noopener">${escapeHTML(source.ledger_id)} · ${escapeHTML(q.research_id)} · open source ↗</a><br>${escapeHTML(source.insight)}</dd>
        <dt>Extracted structure</dt><dd>${escapeHTML(q.structure)}</dd>
        <dt>Novel transformation</dt><dd>${escapeHTML(q.novelty)}</dd>
        <dt>CAT relevance</dt><dd>${escapeHTML(q.cat_relevance)}</dd>
        <dt>CAT difficulty</dt><dd>${escapeHTML(q.cat_difficulty)}</dd>
        <dt>Training difficulty</dt><dd>${escapeHTML(q.training_difficulty)}</dd>
        <dt>Expert method</dt><dd>${escapeHTML(q.expert_method)}</dd>
      </dl></details>`;
    const hintBox = card.querySelector('.pilot-hint');
    const hintButton = card.querySelector('.pilot-hint-button');
    let hintCount = 0;
    hintButton.onclick = () => {
      if (hintCount < q.hints.length) {
        hintBox.hidden = false;
        hintBox.textContent = `Hint ${hintCount+1}: ${q.hints[hintCount]}`;
        hintCount++;
        hintButton.textContent = hintCount < q.hints.length ? `Show hint ${hintCount+1} of ${q.hints.length}` : 'All hints shown';
        hintButton.disabled = hintCount >= q.hints.length;
      }
    };
    card.querySelectorAll('input[type="radio"]').forEach(input => input.onchange = () => {
      card.querySelectorAll('.pilot-option').forEach(label => label.classList.toggle('selected', label.contains(input) && input.checked));
    });
    card.querySelector('.pilot-check').onclick = () => {
      if (card.dataset.answerState === 'checked') return;
      const selectedInput = card.querySelector('input[type="radio"]:checked');
      const result = card.querySelector('.pilot-result');
      if (!selectedInput) { result.hidden = false; result.textContent = 'Choose an option before checking your answer.'; return; }
      card.dataset.answerState = 'checked';
      const selected = Number(selectedInput.value), good = selected === q.answer;
      card.querySelectorAll('.pilot-option').forEach((label,i) => {
        if (i === q.answer) label.classList.add('correct');
        else if (i === selected) label.classList.add('incorrect');
        label.querySelector('input').disabled = true;
      });
      result.hidden = false;
      result.innerHTML = `<strong>${good ? 'Correct.' : 'Canonical answer: '+escapeHTML(q.canonical_answer)+'.'}</strong> ${escapeHTML(q.solution)}<br><strong>Adversarial check:</strong> ${escapeHTML(q.ambiguity_check)}<br><strong>Independent re-solve:</strong> ${escapeHTML(q.independent_solution)}`;
      try {
        if (typeof state !== 'undefined' && Array.isArray(state.events)) {
          const event = {event_id:makeId(),question_key:q.id,section:q.section,is_correct:good,occurred_at:new Date().toISOString()};
          state.events.push(event); recompute(); persist(); paint(); scheduleSync();
        } else {
          const key = 'apex-pilot-attempts';
          const attempts = JSON.parse(localStorage.getItem(key) || '[]');
          attempts.push({question_key:q.id,section:q.section,is_correct:good,occurred_at:new Date().toISOString()});
          localStorage.setItem(key, JSON.stringify(attempts));
        }
      } catch (error) { console.warn('Pilot answer saved to the current view only', error); }
      card.querySelector('.pilot-check').textContent = good ? 'Completed ✓' : 'Reviewed ✓';
      card.querySelector('.pilot-check').disabled = true;
    };
    host.append(card);
  });
};

document.querySelectorAll('[data-pilot-filter]').forEach(button => button.onclick = () => {
  pilotFilter = button.dataset.pilotFilter;
  document.querySelectorAll('[data-pilot-filter]').forEach(item => item.classList.toggle('active', item === button));
  renderPilot();
});

fetch('./pilot.json').then(response => {
  if (!response.ok) throw new Error(`Pilot data request failed (${response.status})`);
  return response.json();
}).then(data => { pilot = data; renderPilot(); }).catch(error => {
  console.error('Research pilot failed to load', error);
  document.querySelector('#pilot-content').innerHTML = '<p class="pilot-loading">The research pilot could not load. Existing quick practice is still available.</p>';
});


