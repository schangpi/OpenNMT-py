# sp.Load("/data/sentence/opennmt_pretrained/sentencepiece.model")
# python process_sentencepiece.py /data/sentence/opennmt_pretrained/sentencepiece.model data/src-val.txt data/srcp-val.txt


# sp.EncodeAsIds("This is a test")
# sp.DecodePieces(['\xe2\x96\x81This', '\xe2\x96\x81is', '\xe2\x96\x81a', '\xe2\x96\x81', 't', 'est'])
# sp.NBestEncode("This is a test", 5)
# sp.DecodeIds([284, 47, 11, 4, 15, 400])
# sp.GetPieceSize()
# sp.IdToPiece(2)
# sp.PieceToId('</s>')
# len(sp)
# sp['</s>']

import sys
import codecs
import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.Load(sys.argv[1])

outfile = codecs.open(sys.argv[3], "w", "utf-8")
with codecs.open(sys.argv[2], "r", "utf-8") as input_file:
    for i, line in enumerate(input_file):
        outfile.write(' '.join(sp.EncodeAsPieces(line)))