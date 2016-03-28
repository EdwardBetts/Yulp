import pytest
from model.feature import FeatureVector, Feature


class TestFeatureVector:
    class BogusFeature(Feature):
        def load(self, path):
            pass

        def train(self, data, labels):
            pass

        def score(self, data):
            return 0.0

        def save(self, path):
            pass

    def test_append(self):
        FeatureVector().append(TestFeatureVector.BogusFeature())

    def test_fail_on_append_non_feature(self):
        with pytest.raises(TypeError):
            FeatureVector().append(0)

    def test_train(self):

        try:

            fv = FeatureVector()
            fv.append(TestFeatureVector.BogusFeature())
            fv.append(TestFeatureVector.BogusFeature())
            fv.append(TestFeatureVector.BogusFeature())
            fv.train([['hello', 'world'], ['this', 'is', 'me']], labels=[])
        except:
            pytest.fail('Training of features failed')

    def test_score(self):
        fv = FeatureVector()
        fv.append(TestFeatureVector.BogusFeature())
        fv.append(TestFeatureVector.BogusFeature())
        fv.append(TestFeatureVector.BogusFeature())
        assert fv.score([[['A']], [['B']], [['C']], [['D']]]) == [[0.0, 0.0, 0.0],
                                                                  [0.0, 0.0, 0.0],
                                                                  [0.0, 0.0, 0.0],
                                                                  [0.0, 0.0, 0.0]]