DIR = '../output/funny_all_2018-07-04_02-29-17-58097/'
FILENAME = DIR+'000_deploy.txt'
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
            if len(params) == 6:
                keyword = params[0]
                docid = params[1]
                entity = params[5]
                if entity == 'O':
                    not_entity_cnt += 1
                else:
                    entity_cnt += 1
                    if keyword not in kes:
                        kes[keyword] = {}
                    if entity not in kes[keyword]:
                        kes[keyword][entity] = 0
                    kes[keyword][entity] += 1
            else:
                pass
    print('all_cnt:', all_cnt)
    print('entity_cnt:', entity_cnt)
    print('not_entity_cnt:', not_entity_cnt)
    print('kes:', len(kes))
    frequent_entity_cnt = 0
    with open(filename+'.kes', 'w') as fout:
        for k,v in kes.items():
            v_sum = 0
            for k1,v1 in v.items():
                #fout.write(k+SEP+k1+SEP+str(v1)+'\n')
                v_sum += v1
            if v_sum >= 100:
                fout.write(k+SEP+str(v_sum)+'\n')
                frequent_entity_cnt += 1
    print('frequent_entity_cnt:', frequent_entity_cnt)

if __name__ == '__main__':
    extract_entity()