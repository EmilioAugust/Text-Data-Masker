from re import compile, sub
from app.models.models import Text, TextOut
from app.patterns.patterns import EMAIL_PATTERN, PHONE_NUMBER_PATTERN, URL_PATTERN

def find_all_matches(pattern, text):
    regex_engine = compile(pattern)
    matches = regex_engine.findall(text)
    return matches

def replace_word(pattern: str, text_to_change: str, text: str):
    return sub(pattern, text_to_change, text)

async def anonymize(text: str, query: str):
    try:
        if text == "":
            return {"message": "Write a text, please."}
        else:
            if query.lower() == "email":
                found_emails = find_all_matches(EMAIL_PATTERN, text)
                new_text = replace_word(EMAIL_PATTERN, "[EMAIL]", text)
                text_out = TextOut(original=text, anonymized=new_text, entities_found=found_emails)

            elif query.lower() == "phone":
                found_phones = find_all_matches(PHONE_NUMBER_PATTERN, text)
                new_text = replace_word(PHONE_NUMBER_PATTERN, "[PHONE]", text)
                text_out = TextOut(original=text, anonymized=new_text, entities_found=found_phones)

            elif query.lower() == "url":
                found_urls = find_all_matches(URL_PATTERN, text)
                new_text = replace_word(URL_PATTERN, "[URL]", text)
                text_out = TextOut(original=text, anonymized=new_text, entities_found=found_urls)
                
            elif query.lower() == "text":
                result_text = text
                report = []

                #email
                found_emails = find_all_matches(EMAIL_PATTERN, text)
                result_text = replace_word(EMAIL_PATTERN, "[EMAIL]", result_text)
                report.append(found_emails)

                #url
                found_urls = find_all_matches(URL_PATTERN, text)
                result_text = replace_word(URL_PATTERN, "[URL]", result_text)
                report.append(found_urls)

                #phone
                found_phones = find_all_matches(PHONE_NUMBER_PATTERN, text)
                result_text = replace_word(PHONE_NUMBER_PATTERN, "[PHONE]", result_text)
                report.append(found_phones)

                text_out = TextOut(original=text, anonymized=result_text, entities_found=report)

            return text_out
    except Exception as e:
        return {"error": f"Error: {e}"}