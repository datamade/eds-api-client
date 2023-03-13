class ResponseTypes():
    def yes_or_no(self, answer):
        if not answer:
            return 'NO'
        else:
            return 'YES'

    def certification(self, answer):
        if not answer:
            return 'I_UNABLE_TO_CERTIFY'
        else:
            return 'I_CERTIFY'

    def disclosure(self, answer):
        if not answer:
            return 'NONE'
        else:
            return 'I_HAVE_A_DISCLOSURE_TO_MAKE'

    def name_response(self, answer):
        return {
            'firstName': answer['first_name'],
            'lastName': answer['last_name']
        }

    def address_response(self, data):
        return {
            'address1': data['address_1'],
            'address2': data['address_2'],
            'city': data['city'],
            'country': data['country'],
            'state': data['state'],
            'zipCode': data['zipcode'],
        }

    def build_complex_response(self, answers, shape):
        """
        Returns a list of complex_responses, based 
        upon the argument "shape", which is a function
        that shapes the response.
        """
        complex_responses = []

        for answer in answers:
            response = shape(answer)
            complex_responses.append(response)

        return complex_responses

    def city_official_compensation_complex(self, answers):

        # Create an anonymous function to be passed into the
        # function that builds the responses. This anonymous function 
        # creates the shape of the response.
        shape = lambda answer: [
            {
                'responseCode': 'ELECTED_OFFICIAL',
                'nameResponse': self.name_response(answer)
            },
            {
                'responseCode': 'INCOME_COMPENSATION',
                'textResponse': answer['description']
            }
        ]
        
        # Pass shape() in to this function and it will help
        # return an array of complex responses.
        complex_response = self.build_complex_response(answers, shape)
        return complex_response

    def city_official_interest_complex(self, answers):

        # TODO: email EKI about exact values because the documentation doesn't give that info
        stakeholder_titles = {
            '511': 'CITY_ELECTED_OFFICIAL',
            '512': 'SPOUSE',
            '513': 'DOMESTIC_PARTNER'
        }

        shape = lambda answer: [
            {
                'responseCode': 'NAME',
                'nameResponse': self.name_response(answer)
            },
            {
                'responseCode': 'ROLE',
                'singleChoosableResponse': stakeholder_titles[answer['position']]
            },
            {
                'responseCode': 'INTERESTS',
                'textResponse': answer['description']
            }
        ]

        complex_response = self.build_complex_response(answers, shape)
        return complex_response

    # TODO: email EKI about the mapping because the values aren't in the documentation
    def family_complex_response(self, answers):
        family_relationships = {
            '222': 'PARENT',
            '223': 'CHILD',
            '224': 'BROTHER',
            '225': 'SISTER',
            '226': 'AUNT',
            '227': 'UNCLE',
            '228': 'NIECE',
            '229': 'NEPHEW',
            '230': 'GRANDPARENT',
            '231': 'GRANDCHILD',
            '232': 'FATHER_IN_LAW',
            '233': 'MOTHER_IN_LAW',
            '234': 'SON_IN_LAW',
            '235': 'DAUGHTER_IN_LAW',
            '236': 'STEPFATHER',
            '237': 'STEPMOTHER',
            '238': 'STEPSON',
            '239': 'STEPDAUGHTER',
            '240': 'STEPBROTHER',
            '241': 'STEPSISTER',
            '242': 'HALF_BROTHER',
            '243': 'HALF_SISTER',
            '250': 'SPOUSE',
            '251': 'DOMESTIC_PARTNER'
        }
        
        family_titles = {
            '244': 'MAYOR',
            '245': 'ALDERMAN',
            '246': 'CITY_CLERK',
            '247': 'CITY_TREASURER',
            '248': 'CITY_DEPARTMENT_HEAD'
        }

        shape = lambda answer: [
            {
                'responseCode': 'CITY_RELATIVES_NAME',
                'nameResponse': self.name_response(answer)
            },
            {
                'responseCode': 'RELATIVES_TITLE',
                'singleChoosableResponse': family_titles[answer['title']]
            },
            {
                'responseCode': 'RELATION_TO_OFFICIAL',
                'singleChoosableResponse': family_relationships[answer['applicant_relationship']],
            }, 
            {
                'responseCode': 'NON-CITY_INDIVIDUAL',
                'nameResponse': self.name_response(answer['applicant'])
            },
            {
                'responseCode': 'INDIVIDUALS_TITLE',
                'textResponse': answer['applicant'].get('title', '')
            },
            {
                'responseCode': 'LEGAL_ENTITY',
                'textResponse': answer.get('legal_entity', '')
            }
        ]

        complex_response = self.build_complex_response(answers, shape)
        return complex_response

    def problem_property_address_response(self, answers):
        shape = lambda answer: [
            {
                'responseCode': 'BUILDING_ADDRESS',
                'addressResponse': self.address_response(answer)
            }
        ]

        complex_response = self.build_complex_response(answers, shape)
        return complex_response

    def employee_complex_response(self, answers):
        shape = lambda answer: [
            {
                'responseCode': 'NAME',
                'nameResponse': self.name_response(answer)
            }, 
            {
                'responseCode': 'CITY_TITLE',
                'textResponse': answer['position']
            }
        ]

        complex_response = self.build_complex_response(answers, shape)
        return complex_response

    def gift_complex(self, answers):
        shape = lambda answer: [
            {
                'responseCode': 'CITY_RECIPIENT',
                'nameResponse': self.name_response(answer)
            },
            {
                'responseCode': 'GIFT_DESCRIPTION',
                'textResponse': answer['gift']
            },
            {
                'responseCode': 'VALUE_OF_GIFT',
                'textResponse': answer['gift_value']
            }
        ]

        complex_response = self.build_complex_response(answers, shape)
        return complex_response

    def retained_name(self, answer, person):
        """Creates a name for the retained entity/person field, because those
        two fields are similar but require different name shapes."""
        if person:
            return {
                'nameResponse': self.name_response(answer)
            }
        else:
            return {
                'textResponse': '{first} {last}'.format(first=answer['first_name'], 
                                                        last=answer['last_name'])
            }

    def retained_complex_response(self, answers, person=False):
        # TODO: email EKI to get the exact values, because they are not in the documentation
        retained_party_roles = {
            '0': 'ACCOUNTANT',
            '1': 'ATTORNEY',
            '2': 'CONSULTANT',
            '3': 'DUMP_SITE',
            '4': 'LOBBYIST',
            '5': 'MWDBE_SUBCONTRACTOR',
            '6': 'NON_MWDBE_SUBCONTRACTOR',
            '7': 'SUPPLIER',
            '8': 'OTHER'
        }

        shape = lambda answer: [
            {
                'responseCode': 'NAME',
                **self.retained_name(answer, person)
            },
            {
                'responseCode': 'ANTICIPATED_RETAINED',
                'singleChoosableResponse': 'RETAINED' if bool(answer['retained']) else 'ANTICIPATED'
            },
            {
                'responseCode': 'BUSINESS_ADDRESS',
                'addressResponse': self.address_response(answer)
            },
            {
                'responseCode': 'RELATIONSHIP',
                'multiChoosableResponse': [retained_party_roles[answer['role']]]
            },
            {
                'responseCode': 'FEES',
                'textResponse': answer['amount_paid']
            },
            {
                'responseCode': 'ESTIMATED_PAID',
                'singleChoosableResponse': 'PAID' if bool(answer['paid']) else 'ESTIMATED'
            }
        ]

        complex_response = self.build_complex_response(answers, shape)
        return complex_response

    def city_official_complex_response(self, answers):
        shape = lambda answer: [
            {
                'responseCode': 'NAME',
                'nameResponse': self.name_response(answer),
            },
            {
                'responseCode': 'BUSINESS_ADDRESS',
                'addressResponse': self.address_response(answer)
            },
            {
                'responseCode': 'NATURE_OF_INTEREST',
                'textResponse': answer['nature_of_interest']
            }
        ]

        complex_response = self.build_complex_response(answers, shape)
        return complex_response
