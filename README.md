# Edge case notes

## Whitespace for NATURE_DISCLOSING_PARTY questionCode

From line 47 of `test_data/valid_eds_submission.json`, the whitespace must exist otherwise it will return a validation error:
```json
{
    "questionCode":"NATURE_DISCLOSING_PARTY       ",
    "singleChoosableResponse":"PERSON_OR_SOLE_PROPRIETOR"
},
```

```python
# they said "The QA operations are actually available @: https://apiqa.chicago.gov/edsapi/rest/.. - see details below."
# is it the same for prod? or will we need to somehow remove "rest" from the url?
url = "{domain}/edsapi/rest/eds/".format(domain=self.domain)
```

- when submitting an invalid password, returns a 500 response with a vague error message >:()
- ditto for submitting a nonexistant username >:() >:() >:()


## There is a typo in one of the question codes, test that this misspelling is required for successful submission
```json
{
    "questionCode":"FINANTIAL_INTEREST",
    "singleChoosableResponse":"YES"
},
```

## No error message for malformed response

Some of the responses look like this:
```
{
   "questionCode":"DBA", 
   "textResponse":"Big Lot Test" 
},
{
    "questionCode":"DISCLOSING_ADDRESS",
        "addressResponse":{
           "address1":"333 N. Lakeshore Drive",
           "address2":"",
           "city":"Chicago",
           "country":"United States",
           "state":"IL",
           "zipCode":"60601"
        }
},
```
In postman, I had to go one by one through each `{…}` and replace the working submission data with the data that my code creates. The bad data was the very last one.

The API gave me no indication of why the request was bad. The request was bad because it was the wrong “response type” expected by the API. It returns a good error messages if the data is missing, but no error message if the data is malformed.


## Misspelling in questionCode
API requires this questionCode misspelling. This will break if they ever change it, but it's spelled this way in the API docs, too.
```json
    {
        'questionCode': 'FINANTIAL_INTEREST',
        'singleChoosableResponse': response_builder.determine_yes_or_no(submission['financial_stakeholders'])
    },
```
