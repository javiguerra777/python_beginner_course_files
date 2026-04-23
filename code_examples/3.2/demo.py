gpa = 3.8
is_senior = False
has_recommendation = True
result = True
# using OR
# if is_senior or has_recommendation:
#     result = True
# using AND
# if gpa > 3.5 and (is_senior or has_recommendation):
#     result = True
# using NOT
if not (gpa > 3.5 and (is_senior or has_recommendation)):
    result = False
print(f"Is student eligible? {result}")