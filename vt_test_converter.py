import unittest
from vt_utils_converter import X3DTranslateToThreeJs


class translateX3D(unittest.TestCase):

    def setUp(self):
        
        self.point = "844134.284462888841517 6516568.605687109753489 0"
        self.line = "<IndexedLineSet  coordIndex='0 1 2 3 4 5 6 7 8'><Coordinate point='844187.943697994574904 6518232.016619521193206 0 844201.841662708669901 6518224.785503129474819 0 844278.95548352599144 6518186.30289267282933 0 844300.016633692430332 6518175.119627367705107 0 844311.424576590536162 6518169.747550436295569 0 844410.036452979431488 6518129.295050370506942 0 844448.537077572080307 6518116.9088667454198 0 844508.316286795539781 6518103.210729259997606 0 844559.869014470255934 6518091.156238601543009 0 ' /></IndexedLineSet> "
        self.lod1 = "<IndexedTriangleSet  index='0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35'><Coordinate point='-149992.141194042400457 7859668.6658656578511 0 -149981.131755757261999 7859668.649239290505648 0 -149981.131755757261999 7859668.649239290505648 8 -149992.141194042400457 7859668.6658656578511 8 -149992.141194042400457 7859668.6658656578511 0 -149981.131755757261999 7859668.649239290505648 8 -149992.125124575686641 7859679.306463955901563 8 -149981.131755757261999 7859668.649239290505648 8 -149981.115686494740658 7859679.289837553165853 8 -149992.125124575686641 7859679.306463955901563 8 -149992.141194042400457 7859668.6658656578511 8 -149981.131755757261999 7859668.649239290505648 8 -149981.115686494740658 7859679.289837553165853 8 -149981.131755757261999 7859668.649239290505648 0 -149981.115686494740658 7859679.289837553165853 0 -149981.115686494740658 7859679.289837553165853 8 -149981.131755757261999 7859668.649239290505648 8 -149981.131755757261999 7859668.649239290505648 0 -149992.125124575686641 7859679.306463955901563 0 -149992.141194042400457 7859668.6658656578511 8 -149992.125124575686641 7859679.306463955901563 8 -149992.125124575686641 7859679.306463955901563 0 -149992.141194042400457 7859668.6658656578511 0 -149992.141194042400457 7859668.6658656578511 8 -149981.115686494740658 7859679.289837553165853 0 -149992.125124575686641 7859679.306463955901563 8 -149981.115686494740658 7859679.289837553165853 8 -149981.115686494740658 7859679.289837553165853 0 -149992.125124575686641 7859679.306463955901563 0 -149992.125124575686641 7859679.306463955901563 8 -149981.131755757261999 7859668.649239290505648 0 -149992.125124575686641 7859679.306463955901563 0 -149981.115686494740658 7859679.289837553165853 0 -149981.131755757261999 7859668.649239290505648 0 -149992.141194042400457 7859668.6658656578511 0 -149992.125124575686641 7859679.306463955901563 0'/></IndexedTriangleSet>"

        self.geomPoint = 'POINT'
        self.geomLine = 'LINESTRING'
        self.geomPolyh = 'POLYHEDRALSURFACE'

        self.resultPoint = """{
    "metadata" :
    {
        "formatVersion" : 3.1,
        "generatedBy"   : "Vizitown Creation",
        "vertices"      : 1,
        "faces"         : 0,
        "normals"       : 0,
        "colors"        : 0,
        "uvs"           : 0,
        "materials"     : 0,
        "morphTargets"  : 0,
        "bones"         : 0
    },

    "vertices" : [844134.284462888841517,6516568.605687109753489,0],

    "morphTargets" : [],

    "normals" : [],

    "colors" : [],

    "uvs" : [],

    "faces" : [],

    "bones" : [],

    "skinIndices" : [],

    "skinWeights" : [],

    "animations" : []

}"""
        self.resultLine = """{
    "metadata" :
    {
        "formatVersion" : 3.1,
        "generatedBy"   : "Vizitown Creation",
        "vertices"      : 9,
        "faces"         : 0,
        "normals"       : 0,
        "colors"        : 0,
        "uvs"           : 0,
        "materials"     : 0,
        "morphTargets"  : 0,
        "bones"         : 0
    },

    "vertices" : [844187.943697994574904,6518232.016619521193206,0,844201.841662708669901,6518224.785503129474819,0,844278.95548352599144,6518186.30289267282933,0,844300.016633692430332,6518175.119627367705107,0,844311.424576590536162,6518169.747550436295569,0,844410.036452979431488,6518129.295050370506942,0,844448.537077572080307,6518116.9088667454198,0,844508.316286795539781,6518103.210729259997606,0,844559.869014470255934,6518091.156238601543009,0],

    "morphTargets" : [],

    "normals" : [],

    "colors" : [],

    "uvs" : [],

    "faces" : [],

    "bones" : [],

    "skinIndices" : [],

    "skinWeights" : [],

    "animations" : []

}"""

        self.resultPolyh = """{
    "metadata" :
    {
        "formatVersion" : 3.1,
        "generatedBy"   : "Vizitown Creation",
        "vertices"      : 36,
        "faces"         : 12,
        "normals"       : 0,
        "colors"        : 0,
        "uvs"           : 0,
        "materials"     : 0,
        "morphTargets"  : 0,
        "bones"         : 0
    },

    "vertices" : [-149992.141194042400457,7859668.6658656578511,0,-149981.131755757261999,7859668.649239290505648,0,-149981.131755757261999,7859668.649239290505648,8,-149992.141194042400457,7859668.6658656578511,8,-149992.141194042400457,7859668.6658656578511,0,-149981.131755757261999,7859668.649239290505648,8,-149992.125124575686641,7859679.306463955901563,8,-149981.131755757261999,7859668.649239290505648,8,-149981.115686494740658,7859679.289837553165853,8,-149992.125124575686641,7859679.306463955901563,8,-149992.141194042400457,7859668.6658656578511,8,-149981.131755757261999,7859668.649239290505648,8,-149981.115686494740658,7859679.289837553165853,8,-149981.131755757261999,7859668.649239290505648,0,-149981.115686494740658,7859679.289837553165853,0,-149981.115686494740658,7859679.289837553165853,8,-149981.131755757261999,7859668.649239290505648,8,-149981.131755757261999,7859668.649239290505648,0,-149992.125124575686641,7859679.306463955901563,0,-149992.141194042400457,7859668.6658656578511,8,-149992.125124575686641,7859679.306463955901563,8,-149992.125124575686641,7859679.306463955901563,0,-149992.141194042400457,7859668.6658656578511,0,-149992.141194042400457,7859668.6658656578511,8,-149981.115686494740658,7859679.289837553165853,0,-149992.125124575686641,7859679.306463955901563,8,-149981.115686494740658,7859679.289837553165853,8,-149981.115686494740658,7859679.289837553165853,0,-149992.125124575686641,7859679.306463955901563,0,-149992.125124575686641,7859679.306463955901563,8,-149981.131755757261999,7859668.649239290505648,0,-149992.125124575686641,7859679.306463955901563,0,-149981.115686494740658,7859679.289837553165853,0,-149981.131755757261999,7859668.649239290505648,0,-149992.141194042400457,7859668.6658656578511,0,-149992.125124575686641,7859679.306463955901563,0],

    "morphTargets" : [],

    "normals" : [],

    "colors" : [],

    "uvs" : [],

    "faces" : [0,0,1,2,0,3,4,5,0,6,7,8,0,9,10,11,0,12,13,14,0,15,16,17,0,18,19,20,0,21,22,23,0,24,25,26,0,27,28,29,0,30,31,32,0,33,34,35],

    "bones" : [],

    "skinIndices" : [],

    "skinWeights" : [],

    "animations" : []

}"""
        self.translator = X3DTranslateToThreeJs()

    # POINT
    def test_out_json_point(self):
        json = self.translator.parse(self.point, self.geomPoint)
        self.assertEqual(json, self.resultPoint)

    def test_nb_vertice_point(self):
        json = self.translator.parse(self.point, self.geomPoint)
        self.assertEqual(self.translator.nbVertices, 1)

    def test_nb_face_point(self):
        json = self.translator.parse(self.point, self.geomPoint)
        self.assertEqual(self.translator.nbFaces, 0)

    # LINE
    def test_out_json_line(self):
        json = self.translator.parse(self.line, self.geomLine)
        self.assertEqual(json, self.resultLine)

    def test_nb_vertice_line(self):
        json = self.translator.parse(self.line, self.geomLine)
        self.assertEqual(self.translator.nbVertices, 9)

    def test_nb_face_line(self):
        json = self.translator.parse(self.line, self.geomLine)
        self.assertEqual(self.translator.nbFaces, 0)

    # POLYHEDRAL
    def test_out_json_polyhedral(self):
        json = self.translator.parse(self.lod1, self.geomPolyh)
        self.assertEqual(json, self.resultPolyhgit)

    def test_nb_vertice_polyhedral(self):
        json = self.translator.parse(self.lod1, self.geomPolyh)
        self.assertEqual(self.translator.nbVertices, 36)

    def test_nb_face_polyhedral(self):
        json = self.translator.parse(self.lod1, self.geomPolyh)
        self.assertEqual(self.translator.nbFaces, 12)

if __name__ == '__main__':
    unittest.main()