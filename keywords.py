# -*- coding: utf-8 -*-
import json
import codecs


class Keywords(object):
    def __init__(self, jsonfile='keywords.json'):
        self.jsonfile = jsonfile
        self.keywords_list = []
        self.load()

        # def __str__(self):
        # return [x.decode('utf8') for x in self.keywords_list]

    def load(self):
        with codecs.open(self.jsonfile, 'r', encoding='utf8') as f:
            self.keywords_list = json.load(f)
            # self.keywords_list = json.load(f, encoding='utf8')
            # json.load()

    def save(self):
        with codecs.open(self.jsonfile, 'w', encoding='utf8') as f:
            json.dump(self.keywords_list, f, encoding='utf8', ensure_ascii=False)

    def add(self, keyword):
        keyword_utf8 = []
        for k in keyword:
            if isinstance(k, unicode):
                keyword_utf8.append(k)
            else:
                keyword_utf8.append(k.decode('utf8'))
        if not self.keywords_list.count(keyword_utf8):
            self.keywords_list.append(keyword_utf8)
        return self

    def delete(self, keyword):
        keyword_utf8 = []
        for k in keyword:
            if isinstance(k, unicode):
                keyword_utf8.append(k)
            else:
                keyword_utf8.append(k.decode('utf8'))
        for i in range(self.keywords_list.count(keyword_utf8)):
            self.keywords_list.remove(keyword_utf8)
        return self


if __name__ == '__main__':
    a = Keywords()
    a.add([u'xbox']).save()
    print(json.dumps(a.keywords_list, encoding='utf8', ensure_ascii=False))


    # print(json.dumps(a.keywords_list, encoding='utf8', ensure_ascii=False))
    #
    # a.add(['abc', 'def']).save()
    # print(json.dumps(a.keywords_list, encoding='utf8', ensure_ascii=False))
    #
    # a.delete(['abc', 'def']).save()
    # print(json.dumps(a.keywords_list, encoding='utf8', ensure_ascii=False))
    #
    # a.delete(["ade", "cde"]).save()
    # print(json.dumps(a.keywords_list, encoding='utf8', ensure_ascii=False))
