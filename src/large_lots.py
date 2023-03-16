from .submission import Submission


class LargeLotsSubmission(Submission):
    def __init__(self):
        super().__init__()

        # hardcoded values
        self.dba('Person or Individual')
        self.fax('')  # required, even if an empty string
        self.po_desc('Purchase of a lot')
        self.city_department('DEPT_OF_PLANNING_AND_DEVELOPMENT')
        self.disclosing_party('PERSON_OR_SOLE_PROPRIETOR')
        self.further_clarifications('I_CERTIFY')
        self.financial_institution('IS_NOT_A_FINANCIAL_INSTITUTION')
        self.slavery('I_CAN_MAKE_THE_ABOVE_VERIFICATION')
        self.federally_funded('NO')
        self.acknowledgements_1('I_ACKNOWLEDGE_CONSENT')
        self.acknowledgements_2('I_ACKNOWLEDGE_CONSENT')
        self.not_a_contractor('NOT_APPLICANT_THAT_IS_A_CONTRACTOR')
        self.general_comment('None')
        self.ethics_detail('N/A')  # api requires a non-empty string
