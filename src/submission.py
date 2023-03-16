import json
from .responses import ResponseTypes


class Submission():
    def __init__(self):
        self._questions = []

    def to_json(self):
        data = {
            'edsQuestions': self._questions
        }
        return json.dumps(data)

    def as_dict(self):
        return {
            'edsQuestions': self._questions
        }

    def dba(self, data):
        self._questions.append({
            'questionCode': 'DBA',
            'textResponse': data
        })

    def disclosing_address(self, data):
        self._questions.append({
            'questionCode': 'DISCLOSING_ADDRESS',
            'addressResponse': ResponseTypes().address_response(data)  # how to make these key names publicly available?
        })

    def phone(self, data):
        self._questions.append({
            'questionCode': 'POC_PHONE',
            'textResponse': data
        })

    def fax(self, data):
        self._questions.append({
            'questionCode': 'POC_FAX',
            'textResponse': data
        })

    def po_desc(self, data):
        self._questions.append({
            'questionCode': 'PO_DESC',
            'textResponse': data
        })

    def spec_num(self, data):
        self._questions.append({
            'questionCode': 'SPEC_NUM',
            'textResponse': data
        })

    def city_department(self, data):
        self._questions.append({
            'questionCode': 'CITY_DEPARTMENT_OR_AGENCY',
            'singleChoosableResponse': data,
        })

    def disclosing_party(self, data):
        self._questions.append({
            # The API requires this whitespace
            'questionCode': 'NATURE_DISCLOSING_PARTY       ',
            'singleChoosableResponse': data,
        })

    # Section III - Income or Compensation to, or Ownership by, City Elected Officials
    def past_income_to_city_official(self, data):
        self._questions.append({
            'questionCode': 'RELATIONSHIP',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def future_income_to_city_official(self, data):
        self._questions.append({
            'questionCode': 'DISCLOSING_PROVIDE_INCOME',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def income_details_to_city_official(self, data):
        if data:
            self._questions.append({
                'questionCode': 'RELATIONSHIP_DETAIL',
                'complexResponse': ResponseTypes().city_official_compensation_complex(data)
            })

    def city_official_financial_interest(self, data):
        self._questions.append({
            # API requires this questionCode misspelling. This will break if
            # they ever change it, but it's spelled this way in the API docs, too.
            'questionCode': 'FINANTIAL_INTEREST',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def city_official_interest_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CITY_OFF_NAMES',
                'complexResponse': ResponseTypes().city_official_interest_complex(data)
            })

    # Section IV - Disclosure of Subcontractors and Other Retained Parties
    def retained_entities(self, data):
        self._questions.append({
            'questionCode': 'RETAINED_ENTITIES_EXIST',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def retained_legal_entities_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'RETAINED_PARTIES_ENTITIES',
                'complexResponse': ResponseTypes().retained_complex_response(data)
            })

    def retained_persons(self, data):
        self._questions.append({
            'questionCode': 'RETAINED_PERSONS_EXIST',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def retained_persons_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'RETAINED_PARTIES_PERSONS',
                'complexResponse': ResponseTypes().retained_complex_response(data, person=True)
            })

    # Section V - Certifications
    def child_support(self, data):
        self._questions.append({
            'questionCode': 'CHILD_SUPPORT',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def child_support_payment(self, data):
        self._questions.append({
            'questionCode': 'PAYMENTSUPPORT',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def further_clarifications(self, data):
        self._questions.append({
            'questionCode': 'FURTHERCLARIFICATIONS',
            'singleChoosableResponse': data,
        })

    def debarment_crimes_civil_judgements(self, data):
        self._questions.append({
            'questionCode': 'CERTIFY1',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def debarment_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CERTIFY1_EXPLAIN',
                'textResponse': data
            })

    def bribery_or_collusion(self, data):
        self._questions.append({
            'questionCode': 'CERTIFY2',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def bribery_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CERTIFY2_EXPLAIN',
                'textResponse': data
            })

    def bid_rigging_and_rotation(self, data):
        self._questions.append({
            'questionCode': 'CERTIFY3',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def bid_rigging_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CERTIFY3_EXPLAIN',
                'textResponse': data
            })

    def sanctions(self, data):
        self._questions.append({
            'questionCode': 'CERTIFY4',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def sanctions_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CERTIFY4_EXPLAIN',
                'textResponse': data
            })

    def crimes_of_dishonesty(self, data):
        self._questions.append({
            'questionCode': 'CERTIFY6',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def crimes_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CERTIFY6_EXPLAIN',
                'textResponse': data
            })

    def employed_city_official(self, data):
        self._questions.append({
            'questionCode': 'CERTIFY7',
            'singleChoosableResponse': ResponseTypes().disclosure(data)
        })

    def employed_city_official_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CERTIFY7_EXPLAIN',
                'complexResponse': ResponseTypes().employee_complex_response(data)
            })

    def tax_and_fee_deliquency(self, data):
        self._questions.append({
            'questionCode': 'H1CERTIFY',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def deliquency_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'H1_EXPLAIN',
                'textResponse': data
            })

    def ethics_and_inspector_general(self, data):
        self._questions.append({
            'questionCode': 'CERTIFY5',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def ethics_detail(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CERTIFY5_EXPLAIN',
                'singleChoosableResponse': data
            })

    def epa_excluded_facilities(self, data):
        self._questions.append({
            'questionCode': 'H2CERTIFY',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def epa_details(self, data):
        if data:
            self._questions.append({
                'questionCode': 'H2_EXPLAIN',
                'textResponse': data
            })

    def contractors_certifications(self, data):
        self._questions.append({
            'questionCode': 'H3CERTIFY',
            'singleChoosableResponse': ResponseTypes().certification(data)
        })

    def contractors_detail(self, data):
        if data:
            self._questions.append({
                'questionCode': '2067',
                'textResponse': data
            })

    def gifts_to_city_employee(self, data):
        self._questions.append({
            'questionCode': 'CERTIFY8',
            'singleChoosableResponse': ResponseTypes().disclosure(data)
        })

    def gifts_detail(self, data):
        if data:
            self._questions.append({
                'questionCode': 'CERTIFY8_EXPLAIN',
                'complexResponse': ResponseTypes().gift_complex(data)
            })

    def financial_institution(self, data):
        self._questions.append({
            'questionCode': 'STATUS_FINANCIAL_INSTITUTION',
            'singleChoosableResponse': data
        })

    def city_official(self, data):
        self._questions.append({
            'questionCode': 'CITY_OFFICIAL',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def city_official_details(self, data):
        self._questions.append({
            'questionCode': 'NAMES_INTERESTS',
            'complexResponse': ResponseTypes().city_official_complex_response(data)
        })

    def future_interest(self, data):
        self._questions.append({
            'questionCode': 'FUTURE_INTEREST',
            'multiChoosableResponse': [ResponseTypes().certification(data)]
        })

    def property_sale(self, data):
        self._questions.append({
            'questionCode': 'PROPERTY_SALE',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def slavery(self, data):
        self._questions.append({
            'questionCode': 'SLAVERY',
            'singleChoosableResponse': data
        })

    def federally_funded(self, data):
        self._questions.append({
            'questionCode': 'FEDERALLY_FUNDED',
            'singleChoosableResponse': data
        })

    def acknowledgements_1(self, data):
        self._questions.append({
            'questionCode': 'ACKNOWLEDGEMENTS',
            'multiChoosableResponse': [data],
        })

    def acknowledgements_2(self, data):
        self._questions.append({
            'questionCode': 'ACKNOWLEDGEMENTS2',
            'multiChoosableResponse': [data]
        })

    # Appendix A
    def family_relationships(self, data):
        self._questions.append({
            'questionCode': 'FAMILIAL_RELATIONSHIP',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def family_detail(self, data):
        if data:
            self._questions.append({
                'questionCode': 'FAMILIAL_RELATIONSHIP_DETAIL',
                'complexResponse': ResponseTypes().family_complex_response(data)
            })

    # Appendix B
    def problem_landlord(self, data):
        self._questions.append({
            'questionCode': 'APBQ1',
            'singleChoosableResponse': ResponseTypes().yes_or_no(data)
        })

    def problem_landlord_name(self, data):
        if data:
            self._questions.append({
                'questionCode': 'APBQ3',
                # this is depedent on there only being one name...
                'complexResponse': [
                    [{
                        'responseCode': 'INDIVIDUAL_NAME',
                        'nameResponse': ResponseTypes().name_response(data)
                    }]
                ]
            })

    def problem_landlord_address(self, data):
        if data:
            self._questions.append({
                'questionCode': 'APBQ4',
                'complexResponse': ResponseTypes().problem_property_address_response(data)
            })

    # Appendix C
    def not_a_contractor(self, data):
        self._questions.append({
            'questionCode': 'APPXC',
            'singleChoosableResponse': data
        })

    def general_comment(self, data):
        self._questions.append({
            'questionCode': 'GENERAL_COMMENT',
            'textResponse': data
        })
