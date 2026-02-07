# General pipeline description
1. data module
   1. data extraction
   2. data preprocessing
2. sequence builder (add special tokens such as separators, delimiter etc...)
   1. 1 sequence
   2. multiview sequence
3. vocab build and tokenizer
   1. special tokens + tokens
   2. tokenizer mapping builder
   3. tokenizer build
4. Pretrain model:
   1. MLM
   2. GPT
   3. JEPA
5. Finetune data module
   1. finetune data build
   2. finetune models
      1. MLP for MLM and GPT
      2. JEPA with new predictor accepting z 
6. patient clustering and phenotype analysis module
   1. patient embedding clustering
   2. cluster feature extraction
   3. statistical analysis
---

Scaffold added by Copilot: minimal Python package, CLI, script and tests to bootstrap development.

Quick start

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Run the pipeline via script

```powershell
python scripts/run_pipeline.py run
```

4. Or run the CLI directly

```powershell
python -m pipeline_hero.cli run
```

Run tests

```powershell
pip install pytest
pytest -q
```

Files added

- `pyproject.toml`: minimal project metadata
- `requirements.txt`: runtime deps
- `.gitignore`: common ignores
- `src/pipeline_hero/`: package with `Pipeline`, `Config`, and `cli`
- `scripts/run_pipeline.py`: convenience entrypoint
- `tests/test_pipeline.py`: simple test

Next steps

- Replace placeholder step implementations in `src/pipeline_hero/pipeline.py` with real extraction/transform/load logic
- Add configuration parsing and unit tests for each component
- Wire CI and packaging as needed