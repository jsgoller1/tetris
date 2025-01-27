from src.render_data import ScoreboardRenderData


class ScoreKeeper:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lines_cleared = 0

    def add_cleared_lines(self, num_lines: int):
        """Update score and level when lines are cleared"""
        if num_lines == 0:
            return

        # Classic NES Tetris scoring
        line_scores = {1: 40, 2: 100, 3: 300, 4: 1200}

        # Add to score (multiplied by current level)
        self.score += line_scores.get(num_lines, 0) * self.level

        # Update lines cleared
        self.lines_cleared += num_lines

        # Update level (every 10 lines)
        self.level = (self.lines_cleared // 10) + 1

    def get_render_data(self) -> ScoreboardRenderData:
        """Get the current score data for rendering"""
        return ScoreboardRenderData(
            score=self.score, level=self.level, lines_cleared=self.lines_cleared
        )
