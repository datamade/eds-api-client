import uuid
import random

def unique_applicant():
    idx = str(uuid.uuid4()).split('-')[0]
    username = 'edsreserverd_dmt_{}'.format(idx)
    email_address = 'testing+{}@datamade.us'.format(idx)

    dummy_ssn = ''.join([str(random.randint(0, 9)) for i in range(0, 9)])
    formatted_ssn = '%s-%s-%s' % (dummy_ssn[0:3], dummy_ssn[3:5], dummy_ssn[5:])
    
    return username, email_address, formatted_ssn
