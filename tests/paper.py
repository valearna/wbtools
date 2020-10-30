import os
import unittest

from wbtools.literature.paper import WBPaper

TESTDATA_DIR = os.path.join(os.path.dirname(__file__), 'data', 'text_files')


class TestWBPaper(unittest.TestCase):

    def test(self):
        paper = WBPaper()
        paper.add_file(dir_path=TESTDATA_DIR, filename='00026804_McCracken05.txt', remote_file=False, pdf=False)
        self.assertTrue(paper.has_same_wbpaper_id_as_filename('00026804_McCracken05.txt'))
        paper.add_file(dir_path=TESTDATA_DIR, filename='00026804_McCracken05_supp.txt', remote_file=False, pdf=False)
        self.assertEqual(len(paper.get_text_docs(remove_ref_section=False, split_sentences=False, lowercase=False,
                                                 tokenize=False, remove_stopwords=False, remove_alpha=False)), 2)
        self.assertTrue("REFERENCES" not in "\n\n".join(
            paper.get_text_docs(remove_ref_section=True, split_sentences=False, lowercase=False, tokenize=False,
                                remove_stopwords=False, remove_alpha=False)))
        self.assertGreater(len(paper.get_text_docs(remove_ref_section=False, split_sentences=True, lowercase=False,
                                                   tokenize=False, remove_stopwords=False, remove_alpha=False)), 2)
        self.assertTrue("\n\n".join(
            paper.get_text_docs(remove_ref_section=False, split_sentences=False, lowercase=True, tokenize=False,
                                remove_stopwords=False, remove_alpha=False)).islower())
        self.assertTrue(type(paper.get_text_docs(remove_ref_section=False, split_sentences=False, lowercase=False,
                                                 tokenize=True, remove_stopwords=False, remove_alpha=False)[0]) is list)
        self.assertTrue("." in paper.get_text_docs(remove_ref_section=False, split_sentences=False, lowercase=False,
                                                   tokenize=True, remove_stopwords=False, remove_alpha=False)[0])
        self.assertTrue("we" not in paper.get_text_docs(remove_ref_section=False, split_sentences=False,
                                                        lowercase=False, tokenize=True, remove_stopwords=True,
                                                        remove_alpha=False)[0])
        self.assertTrue("." not in paper.get_text_docs(remove_ref_section=False, split_sentences=False, lowercase=False,
                                                       tokenize=True, remove_stopwords=True, remove_alpha=True)[0])
