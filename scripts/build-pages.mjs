import { cp, mkdir, rm } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const output = resolve(root, 'dist');
if (!output.startsWith(`${root}${process.platform === 'win32' ? '\\' : '/'}`)) {
  throw new Error('Refusing to write outside the repository');
}

await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });
for (const file of ['index.html', 'app.js', 'pilot-app.js', 'styles.css', 'sw.js', 'manifest.webmanifest', 'icon.svg']) {
  await cp(join(root, file), join(output, file));
}
await cp(join(root, 'vendor'), join(output, 'vendor'), { recursive: true });
await cp(join(root, 'research', 'pilot', 'pilot.json'), join(output, 'pilot.json'));
console.log(`Prepared static Pages bundle at ${output}`);

