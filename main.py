from logic import matching

ar = matching()

s1 = "apa topik teman abai ?"
s2 = "abai temannya topik apa itu benar ?"

print('ratio : ',ar.simple_ratio(s1,s2))
print('partial ratio : ',ar.partial_ratio(s1,s2))
print('short ratio : ',ar.short_ratio(s1,s2))
print('partial short ratio : ',ar.partial_short_ratio(s1,s2))
print('token ratio : ',ar.token_ratio(s1,s2))
print('partial token ratio : ',ar.partial_token_ratio(s1,s2))
