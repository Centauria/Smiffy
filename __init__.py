# -*- coding: utf-8 -*-
import random;

CMD=['dc', 'sl', 'fjp', 'hcp'];

def onQQMessage(bot, contact, member, content):
    if contact.ctype=='group' and contact.qq=='572661635':
        draw(bot, contact, member, content);

def draw(bot, contact, member, cmd):
    if cmd in CMD:
        if cmd=='dc':
            bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+dc());
        elif cmd=='sl':
            bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+sl());
        elif cmd=='fjp':
            bot.SendTo(contact,'@'+member.name+'的'+cmd+'结果：\n'+fjp());
        elif cmd=='hcp':
            bot.SendTo(contact, '@'+member.name+'的'+cmd+'结果：\n'+hcp());

def dc():
    prob=random.randint(0, 100);
    if prob<10:
        result='UR';
    elif prob<30:
        result='SSR';
    elif prob<60:
        result='SR';
    else:
        result='R';
    return result;

def sl():
    res={'UR':0, 'SSR':0, 'SR':0, 'R':0};
    result='';
    for i in range(11):
        res[dc()]+=1;
    result='UR=%d  SSR=%d  SR=%d  R=%d'%(res['UR'], res['SSR'],res['SR'], res['R']); 
    return result;

def fjp():
    prob=random.randint(0, 100);
    if prob<50:
        result='UR';
    else:
        result='SR';
    return result;

def hcp():
    prob=random.randint(0, 100);
    if prob<30:
        result='UR';
    elif prob<60:
        result='SSR';
    else:
        result='SR';
    return result;
