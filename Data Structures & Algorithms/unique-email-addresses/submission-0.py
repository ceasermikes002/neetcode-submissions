class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')
            #Build cleaned local part while processing
            cleaned_local = []
            for char in local:
                if char == '+':
                    break
                if char != '.':
                    cleaned_local.append(char)
            cleaned_email = ''.join(cleaned_local) + '@' + domain
            unique_emails.add(cleaned_email)

        return len(unique_emails)        