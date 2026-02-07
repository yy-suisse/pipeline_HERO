from pipeline_hero.pipeline import Pipeline


def test_pipeline_runs():
    p = Pipeline()
    p.run()
    assert True
