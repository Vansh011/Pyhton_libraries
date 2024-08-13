class Charge:
    def __init__(self, card_country, currency, amount, ip_country):
        self.card_country = card_country
        self.currency = currency
        self.amount = amount
        self.ip_country = ip_country

    @classmethod
    def from_string(cls, charge_str):
        params = charge_str.split('&')
        card_country = params[0].split('=')[1]
        currency = params[1].split('=')[1]
        amount = int(params[2].split('=')[1])
        ip_country = params[3].split('=')[1]
        return cls(card_country, currency, amount, ip_country)

class RadarRules:
    def __init__(self, rules):
        self.rules = rules
        self.charge = None

    def evaluate(self):
        for rule in self.rules:
            if rule.startswith("CHARGE"):
                self.charge = Charge.from_string(rule.split(":")[1].strip())
            elif rule.startswith("ALLOW"):
                if self._evaluate_condition(rule.split(":")[1].strip()):
                    return 1
            elif rule.startswith("BLOCK"):
                if self._evaluate_condition(rule.split(":")[1].strip()):
                    return 0
        return 1  # Default to allow if no blocking condition met

    def _evaluate_condition(self, condition):
        # Handle AND conditions
        if " AND " in condition:
            conditions = condition.split(" AND ")
            return all(self._evaluate_single_condition(cond.strip()) for cond in conditions)
        else:
            return self._evaluate_single_condition(condition.strip())

    def _evaluate_single_condition(self, condition):
        if ">" in condition:
            field, value = condition.split(">")
            return int(self._get_field_value(field.strip())) > int(value.strip())
        elif "<" in condition:
            field, value = condition.split("<")
            return int(self._get_field_value(field.strip())) < int(value.strip())
        elif "!=" in condition:
            field, value = condition.split("!=")
            return self._get_field_value(field.strip()) != value.strip()
        elif "==" in condition:
            field, value = condition.split("==")
            return self._get_field_value(field.strip()) == value.strip()
        return False

    def _get_field_value(self, field):
        if field == "amount":
            return self.charge.amount
        elif field == "card_country":
            return self.charge.card_country
        elif field == "ip_country":
            return self.charge.ip_country
        elif field == "currency":
            return self.charge.currency
        return None

# Example usage
rules = [
    "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
    "ALLOW:amount<100",
    "BLOCK:card_country != ip_country AND amount > 100"
]

radar = RadarRules(rules)
result = radar.evaluate()
print(result)  # Output: 0 (Blocked)


# You are given a system that evaluates financial transactions based on a set of rules. Each transaction has details such as the card's country of origin, the currency used, the transaction amount, and the IP country from which the transaction is initiated. The system needs to determine whether to allow or block a transaction based on these details.

# You need to implement a method that processes a list of rules and decides the outcome of a transaction. The rules are provided as strings in the format:

# "CHARGE: card_country=XX&currency=XXX&amount=NNN&ip_country=YY"
# "ALLOW:condition"
# "BLOCK:condition"
# Example Input:
# java
# Copy code
# String[] values = {
#     "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
#     "ALLOW:amount<100",
#     "BLOCK:card_country != ip_country AND amount > 100"
# };
# Example Output:
# The method should return 0 if the transaction is blocked.
# The method should return 1 if the transaction is allowed.
# Key Points to Discuss:
# String Parsing: How would you efficiently parse and extract relevant fields from the input strings?
# Condition Evaluation: How do you plan to evaluate the conditions dynamically, especially when multiple conditions are combined (e.g., card_country != ip_country AND amount > 100)?
# Edge Cases: What edge cases do you consider, such as invalid formats or unexpected conditions?
# Example Code Execution:
# Given the following rules and input:

# java
# Copy code
# String[] values = {
#     "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
#     "BLOCK:amount > 100"
# };
# Expected Output: 0 (since the transaction amount exceeds 100, it is blocked).

# Given the following more complex rule set:

# java
# Copy code
# String[] values = {
#     "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
#     "ALLOW:amount<100",
#     "BLOCK:card_country != ip_country AND amount > 100"
# };
# Expected Output: 0 (since the card country differs from the IP country and the amount is greater than 100, it is blocked).

# Further Discussion:
# Design Decisions: How do you structure your classes and methods to ensure scalability and maintainability?
# Optimizations: How can the solution be optimized for performance, especially when handling large sets of rules and transactions?
# This question allows the interviewee to demonstrate their understanding of string manipulation, condition evaluation, and object-oriented design, which are crucial for handling complex business logic.