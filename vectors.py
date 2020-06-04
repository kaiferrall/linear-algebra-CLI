
def read_vector(self, vs):
    try:

        v = vs.split(' ')
        res = []

        for n in v:
            try:
                res.append(float(n))
            except Exception as e:
                pass

        return res

    except Exception as e:
        raise Exception('Invalid vector string.')

