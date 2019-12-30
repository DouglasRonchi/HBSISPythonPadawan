import unittest

from app.terminal.terminal import Terminal


class TestTerminal(unittest.TestCase):
    def test_terminal_nao_deveria_ter_elementos(self):
        terminal = Terminal()
        self.assertEqual(len(terminal.get_elementos()), 0)
