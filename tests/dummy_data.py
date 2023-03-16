import uuid
import os

SESSION_DATA = {
    'tracking_id': uuid.uuid4(),
    'applicant': {
        'first_name': 'hannah',
        'middle_name': '',
        'last_name': 'cushman',
        'username': os.environ['TEST_VENDOR_USERNAME'],
        'password': os.environ['TEST_VENDOR_PASSWORD'],
        'secret_question': 1,
        'secret_answer': 'chicago',
        'ssn': '123-99-9999',
        'telephone_number': '123-456-7890',
        'email_address': 'hannah.cushman@datamade.us',
        'address_1': '123 S Main',
        'address_2': '',
        'address_3': '',
        'city': 'Chicago',
        'state': 'IL',
        'zipcode': '12345',
        'country': 'United States'
    },
    'city_employee': {
        'city_employee': 0
    },
    'income_or_compensation': {
        'boolean': 1,
        'income_or_compensation': [
            {
                'first_name': 'Derek',
                'last_name': 'Eder',
                'relationship_type': 'past',  # past or anticipated
                'description': 'I raked his leaves.'
            }
        ]
    },
    'employees': {
        'boolean': 1,
        'employees': [
            {
                'first_name': 'Rahm',
                'last_name': 'Emanuel',
                'position': 'Mayor'
            }
        ]
    },
    'financial_obligation': {
        'boolean': 1,
        'financial_obligation': [
            {
                'first_name': 'Regina',
                'last_name': 'Compton',
                'position': '511',
                'description': 'I rent my apartment from her.'
            }
        ]
    },
    'gifts': {
        'boolean': 1,
        'gifts': [
            {
                'first_name': 'Derek',
                'last_name': 'Eder',
                'gift': 'Time',
                'gift_value': '$400'
            }
        ]
    },
    'family': {
        'boolean': 1,
        'family': [
            {
                'first_name': 'Anna',
                'last_name': 'Valencia',
                'title': '246',
                'applicant_relationship': '225'
            }
        ]
    },
    'retained_parties': {
        'boolean': 1,
        'retained_parties': [
            {
                'first_name': 'Eric',
                'last_name': 'van Zanten',
                'role': '4',
                'address_1': '123 N Main',
                'address_2': '',
                'address_3': '',
                'city': 'Chicago',
                'state': 'IL',
                'zipcode': '12345',
                'country': 'United States',
                'party_type': 'individual',
                'retained': 0,
                'paid': 0,
                'amount_paid': '$25'
            }
        ]
    },
    'individual_criminal_history': {
        'individual_criminal_history': {
            'boolean': 0,
            'expl': ''
        }
    },
    'group_criminal_history': {
        'group_criminal_history': {
            'boolean': 1,
            'expl': 'live together, die alone'
        }
    },
    'disqualifications': {
        'bid_rigging': {
            'boolean': 0,
            'expl': ''
        },
        'sanctions_list': {
            'boolean': 1,
            'expl': '"most likely to succeed"'
        }
    },
    'problem_properties': {
        'boolean': 1,
        'problem_properties': [
            {
                'address_1': '456 S Main',
                'address_2': '',
                'address_3': '',
                'city': 'Chicago',
                'state': 'IL',
                'zipcode': '34567',
                'country': 'United States'
            }
        ]
    },
    'conduct_compliance': {
        'conduct_compliance': {
            'boolean': 0,
            'expl': ''
        }
    },
    'child_support_compliance': {
        'behind_on_child_support': 0
    },
    'payment_and_hiring_compliance': {
        'payment_compliance': {
            'boolean': 0,
            'expl': ''
        },
        'environmental_compliance': {
            'boolean': 1,
            'expl': "don't tread on me"
        },
        'hiring_compliance': {
            'boolean': 0,
            'expl': ''
        }
    },
    'closing_acknowledgements': {
        'void_if_false': 'y',
        'kept_current': 'y',
        'public_record': 'y',
        'part_of_contract': 'y',
        'ethics_acknowledgement': 'y'
    },
    'signature': 'hannah'
}

EDS_DATA = {
    'applicant': {
        'first_name': 'hannah',
        'middle_name': '',
        'last_name': 'cushman',
        'username': os.environ['TEST_VENDOR_USERNAME'],
        'password': os.environ['TEST_VENDOR_PASSWORD'],
        'secret_question': 1,
        'secret_answer': 'chicago',
        'ssn': '123-45-9999',
        'telephone_number': '123-456-7890',
        'email_address': 'hannah.cushman@datamade.us',
        'address_1': '123 S Main',
        'address_2': '',
        'address_3': '',
        'city': 'Chicago',
        'state': 'IL',
        'zipcode': '12345',
        'country': 'United States'
    },
    'city_employee': True,
    'compensated_officials': [
        {
            'first_name': 'Eric',
            'last_name': 'van Zanten',
            'description': 'MC (Master of Cemeteries)',
            'relationship_type': 'past'  # past or anticipated
        }
    ],
    'financial_stakeholders': [
        {
            'first_name': 'Rahm',
            'last_name': 'Emanuel',
            'position': '511',
            'description': 'I rake his leaves.'
        }
    ],
    'retained_legal_entities': [
        {
            'first_name': 'Hannah',
            'last_name': 'Cushman',
            'address_1': '123 Main St',
            'address_2': '',
            'address_3': '',
            'city': 'Chicago',
            'state': 'IL',
            'zipcode': '60640',
            'country': 'United States',
            'retained': True,
            'amount_paid': '$2500',
            'paid': False,
            'role': '2'
        }
    ],
    'retained_persons': [
        {
            'first_name': 'Forest',
            'last_name': 'Gregg',
            'address_1': '456 Oak St',
            'address_2': '',
            'address_3': '',
            'city': 'Chicago',
            'state': 'IL',
            'zipcode': '60605',
            'country': 'United States',
            'retained': False,
            'amount_paid': '$600',
            'paid': True,
            'role': '1'
        }
    ],
    'employees': [
        {
            'first_name': 'Jean',
            'last_name': 'Cochrane',
            'position': 'Pro Dr Martens wearer'
        },
        {
            'first_name': 'Regina',
            'last_name': 'Compton',
            'position': 'Fellow soup eater'
        }
    ],
    'gifts': [
        {
            'first_name': 'Derek',
            'last_name': 'Eder',
            'gift': 'Civic organizing',
            'gift_value': 'Priceless'
        }
    ],
    'family': [
        {
            'first_name': 'Megan',
            'last_name': 'Cushman',
            'title': '248',
            'applicant_relationship': '225'
        }
    ],
    'problem_properties': [
        {
            'address_1': '2153 Bayard Park Dr',
            'address_2': '',
            'address_3': '',
            'city': 'Evansville',
            'state': 'IN',
            'zipcode': '47714',
            'country': 'United States'
        }
    ],

    # bool
    'behind_on_child_support': False,
    'in_agreement_to_repay_child_support': False,

    'individual_criminal_history': True,
    'group_criminal_history': False,
    'bid_rigging': False,
    'sanctions_list': False,

    'conduct_compliance': False,
    'payment_compliance': True,
    'environmental_compliance': False,
    'hiring_compliance': False,

    # str
    'individual_criminal_history_expl': 'my twenties were wild',
    'group_criminal_history_expl': None,
    'bid_rigging_expl': None,
    'sanctions_list_expl': None,

    'conduct_compliance_expl': None,
    'payment_compliance_expl': 'don\'t tread on me',
    'environmental_compliance_expl': None,
    'hiring_compliance_expl': None
}
