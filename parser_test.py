import os
import unittest
import sys
import subprocess as sub

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.output = "b'PR: 4\\nSC: 9\\nSP: 1\\n'" 
    
    """
    Test for local files
    """
    def test_main_local_json(self):
        """
        Test the json local file loaded
        """
        #result = os.system("python parser.py /usr/src/myapp/conteudo.json")
        p = sub.Popen(["python", "parser.py", "/usr/src/myapp/conteudo.json"],stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        
        self.assertEqual(str(output), self.output)

    def test_main_local_csv(self):
        """
        Test the json local file loaded
        """
        #result = os.system("python parser.py /usr/src/myapp/conteudo.json")
        p = sub.Popen(["python", "parser.py", "/usr/src/myapp/conteudo.csv"],stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        
        self.assertEqual(str(output), self.output)
 
    """
    Test for remote files
    """
    def test_main_remote_json(self):
        """
        Test the json remote file loaded
        """
        remote = "https://gist.githubusercontent.com/israelbgf/fbdb325cd35bc5b956b2e350d354648a/raw/b26d28f4c01a1ec7298020e88a200d292293ae4b/conteudojson"
        #result = os.system("python parser.py /usr/src/myapp/conteudo.json")
        p = sub.Popen(["python", "parser.py", remote],stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        
        self.assertEqual(str(output), self.output)
 
    def test_main_remote_csv(self):
        """
        Test the csv remote file loaded
        """
        remote = "https://gist.githubusercontent.com/israelbgf/782a92243d0ba1ff47f9aaf46358f870/raw/86c7a2bf04242bd4262b203ca725ce1da69f035d/conteudocsv"
        #result = os.system("python parser.py /usr/src/myapp/conteudo.json")
        p = sub.Popen(["python", "parser.py", remote],stdout=sub.PIPE,stderr=sub.PIPE)
        output, errors = p.communicate()
        
        self.assertEqual(str(output), self.output)

if __name__ == '__main__':
    unittest.main()