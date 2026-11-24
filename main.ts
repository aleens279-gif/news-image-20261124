// main.ts — entrypoint for the make.fun news-image bounty.
// Copies the pre-rendered front page (entry.png, in this directory) to
// /output/entry.png. No dependencies, no network, deterministic: both runs
// write identical bytes. MAKEFUN_OUTPUT overrides the destination for
// local testing only.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const out = process.env.MAKEFUN_OUTPUT || "/output/entry.png";
mkdirSync(dirname(out), { recursive: true });
copyFileSync(join(here, "entry.png"), out);
