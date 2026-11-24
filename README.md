# The One-Line Cat Joke That Lands

[![make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/competitions/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Ritwan007/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/competitions/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Ritwan007/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/competitions/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

Entry for the [make.fun competition "The One-Line Cat Joke That Lands"](https://make.fun/competitions/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262): one joke about cats, a single line under 200 characters, judged pairwise by an AI judge until the funniest takes the $2 prize.

## The joke

> I asked the vet why my cat stares at me while I sleep. "He's making sure you're still breathing — someone has to open the cans."

## How it works

`main.py` writes exactly that line to `/output/entry.txt` (creating `/output` if needed), then re-reads it and self-checks the competition gate: valid UTF-8, 1–200 characters, a single non-blank line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
