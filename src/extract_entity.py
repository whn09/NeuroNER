DIR = '../output/funny_all_2018-07-04_02-29-17-58097/'
FILENAME = dir+'000_deploy.txt'
SEP = ' '


def extract_entity(filename=FILENAME):
    all_cnt = 0
    entity_cnt = 0
    not_entity_cnt = 0
    kes = {}
    with open(filename, 'r') as fin:
        lines = fin.readlines()
        for line in lines:
            all_cnt += 1
            params = line.strip().split(SEP)
            if len(params) == 7:
                entity_cnt += 1
                keyword = params[0]
                docid = params[1]
                entity = params[6]
                if keyword not in kes:
                    kes[keyword] = entity
                else:
                    if kes[keyword] != entity:
                        print(keyword, kes[keyword], entity)
            if len(params) == 6:
                not_entity_cnt += 1
            else:
                pass
    print('kes:', len(kes))
    with open(filename+'.kes', 'w') as fout:
        for k,v in kes.items():
            fout.write(k+SEP+v+'\n')


if __name__ == '__main__':
    extract_entity()