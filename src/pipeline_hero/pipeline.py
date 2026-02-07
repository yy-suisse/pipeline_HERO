from .config import Config


class Pipeline:
    def __init__(self, config: Config | None = None):
        self.config = config or Config()

    def run(self):
        print("[pipeline] Running pipeline with config:", self.config)
        self.step_extract()
        self.step_transform()
        self.step_load()

    def step_extract(self):
        print("[pipeline] Extract: placeholder implementation")

    def step_transform(self):
        print("[pipeline] Transform: placeholder implementation")

    def step_load(self):
        print("[pipeline] Load: placeholder implementation")



