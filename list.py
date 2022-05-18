student_score = [70,80,55]
name = ['min','nok','james']
mix = [1,3.5,'mint',[1,2,3]]
distance = [9,8,7,6,5]
del distance[2]
print(f"""

{student_score[2]}
{student_score}
{type(student_score)}

{name[0]}
{name[-1]}
{name[-1][-2]}
{name}
{type(name)}

{mix[2][3]}
{mix[3][1]}
{mix}
{type(mix)}

{distance}

"""
)