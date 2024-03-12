import unittest
from src.downer import downer


class TestBasicConversion(unittest.TestCase):
    def test_total_conversion(self):
        tests = [
            ('This next word is **bold** but no others', 'This next word is <strong>bold</strong> but no others'),
            (r"This \**shouldn't be bold, but **this should be**. Nice!", r"This \**shouldn't be bold, but <strong>this should be</strong>. Nice!"),
            ('This is *italics*, this is __bold__', 'This is <em>italics</em>, this is <strong>bold</strong>'),
            ('', ''),
            ('No markdown here!', 'No markdown here!'),
            ('Trailing **bold will keep going but automatically terminate', 'Trailing <strong>bold will keep going but automatically terminate</strong>'),
            ('This is ***bold and italic***. Cool.', 'This is <strong><em>bold and italic</strong></em>. Cool.'),
        ]

        for test in tests:
            self.assertEqual(test[1], downer.convert(test[0]))

    def test_bold(self):
        tests = [
            ('This next word is **bold** but no others', 'This next word is <strong>bold</strong> but no others'),
            (r"This \**shouldn't be bold, but **this should be**. Nice!", r"This \**shouldn't be bold, but <strong>this should be</strong>. Nice!"),
            ('This is *italics*, this is **bold**', 'This is *italics*, this is <strong>bold</strong>'),
            ('', ''),
            ('No bold here!', 'No bold here!'),
            ('Trailing **bold will keep going but automatically terminate', 'Trailing <strong>bold will keep going but automatically terminate</strong>'),
            ('This is ***bold*** and leaves uninterpreted italics', 'This is <strong>*bold</strong>* and leaves uninterpreted italics')
        ]

        for test in tests:
            self.assertEqual(test[1], downer._find_bold(test[0]))

    def test_italics(self):
        tests = [
            ('This next word is *italic* but no others', 'This next word is <em>italic</em> but no others'),
            (r"This \*shouldn't be italic, but *this should be*. Nice!", r"This \*shouldn't be italic, but <em>this should be</em>. Nice!"),
            ('', ''),
            ('No italics here!', 'No italics here!'),
            ('Trailing *italics will keep going but automatically terminate', 'Trailing <em>italics will keep going but automatically terminate</em>'),
            ('This is <strong>*bold</strong>* and leaves uninterpreted italics', 'This is <strong><em>bold</strong></em> and leaves uninterpreted italics'),
            # markdownguide.org tests
            ("Italicized text is the *cat's meow*.", "Italicized text is the <em>cat's meow</em>."),
            ("Italicized text is the _cat's meow_.", "Italicized text is the <em>cat's meow</em>."),
            ("A*cat*meow", "A<em>cat</em>meow")
        ]

        for test in tests:
            self.assertEqual(test[1], downer._find_italics(test[0]))

    @unittest.skip('Mismatching underscores and asterisks is currently undefined behavior.')
    def test_emphasis_tag_mismatch(self):
        self.assertEqual('_italics_, _not italic*', '<em>italics</em>, _not italic*')
        self.assertEqual('__bold__, __not bold**', '<strong>bold</strong>, __not bold**')

    @unittest.skip('Unmatched tag will create an empty but unnecessary tag')
    def test_unmatched_tag_at_end(self):
        self.assertEqual(r'No bold tags**', r'No bold tags**')


if __name__ == '__main__':
    unittest.main()
