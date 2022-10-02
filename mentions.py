members = ['id123','id234','id7','id321']
messages = [
    "Hey @id123,id321 review this pr please! @id123 what do you think about this approach",
    "Hey @id7 nice appro@ch! Great job! @id800 what do you think",
    "@id123,id321 thnx"
    ]
def frequency(members,messages):
    count = {x:0 for x in members}
    def check_mention(word):
        if word[0:3] == '@id':
            return True
        else:
            False
    for message in messages:
        alreadyMentioned = [];
        mentionList = (list(filter(check_mention,message.split())))
        for mention in mentionList:
            mention = mention[1:];
            for single in mention.split(','):
                if single not in alreadyMentioned:
                    alreadyMentioned.append(single)
        for finalCount in alreadyMentioned:
            if finalCount in count:
                count[finalCount] += 1
    count = sorted(count.items(),key = lambda x: x[1], reverse = 1)
    return [x[0]+'='+str(x[1]) for x in count];

print (frequency(members,messages));
