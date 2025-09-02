    # 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
define all_song = "audio/Daldameowsic_#11키위.mp3"
define end_song = "audio/Daldameowsic_#26벚꽃.mp3"


init python :
    chooseTang = 0
        
# 게임에서 사용할 캐릭터를 정의합니다.
define pat = Character('박소단', color="#420417", who_outlines=[(absolute(2),"#a7586f",absolute(0),absolute(0))])
define shu = Character('유수림', color="#f5cc4f")
define pi = Character('전도하', color="#be2a2a")
define cho = Character('윤정제', color="#362218", who_outlines=[(absolute(2),"#a06f57",absolute(0),absolute(0))])
define tang = Character('이 현', color="#efb750")
define boong = Character('붕선생', color="#c37d0d")
define pname = "플레이어 이름"
define p = Character('pname', dynamic = True, color="#440eb1", who_outlines=[(absolute(1),"#c3a4ff",absolute(0),absolute(0))])
define ac = Character() #행동



#charecter
image c_pat_n = im.FactorScale("pat_n.png", 1)
image c_pat_m = im.FactorScale("pat_m.png", 1)
image c_pat_m = im.FactorScale("pat_m.png", 1)
image c_pat_h = im.FactorScale("pat_h.png", 1)

image c_shu_n = im.FactorScale("shu_n.png", 0.81)
image c_shu_h = im.FactorScale("shu_h.png", 0.81)
image c_shu_m = im.FactorScale("shu_m.png", 0.81)

image c_cho_n = im.FactorScale("cho_n.png", 0.88)
image c_cho_h = im.FactorScale("cho_h.png", 0.88)
image c_cho_m = im.FactorScale("cho_m.png", 0.88)

image c_pi_n = im.FactorScale("pi_n.png", 0.88)
image c_pi_h = im.FactorScale("pi_h.png", 0.88)
image c_pi_m = im.FactorScale("pi_m.png", 0.88)

image c_tang_n = im.FactorScale("tang_n.png", 1)
image c_tang_h = im.FactorScale("tang_h.png", 1)

define p_center = Position(xalign=0.5,yalign=0.48)
define s_center = Position(xalign=0.5,ypos=1.05)
define c_center = Position(xalign=0.38,ypos=1.05)
define pi_center = Position(xalign=0.38,ypos=1.05)
define t_center = Position(xalign=0.5,yalign=0.48)

image c_boong = im.FactorScale("bnoog.png", 1)


#background image
image bg_class_1 = "classroom1.png"
image bg_class_2 = "classroom2.png"
image bg_class_3 = "classroom4.png"
image bg_nclass_1 = "classroomn1.png"
image bg_nclass_2 = "classroomn2.png"
image bg_atelier = "Atelier1.png"
image bg_cafe_m = "cafe1.png"
image bg_cafe_e = "cafe2.png"
image bg_boong = "teacher.png"
image bg_dess = "dessert.png"
image bg_mstreet = "moningst.png"
image bg_nstreet = "night.png"
image bg_shuroom = "shuroom.png"
image bg_ground = "ground.png"
image bg_bokdo = "corridor.png"
image bg_lid = "library.png"

#exrta
image main = "main.png"
image game_over = "gui/game_over.png"
image pat_1 = "pat_get1.png"
image shu_1 = "shu_get1.png"
image pizza_1 = "pizza_get1.png"
image cho_1 = "cho_get1.png"
define pat_1_center = Position(xalign=0.5, yalign=0.5)
define pizza_1_center = Position(xalign=0.5, yalign=0.5)
define shu_1_center = Position(xalign=0.5, yalign=0.5)
define cho_1_center = Position(xalign=0.5, yalign=0.5)


init python:
    item_boong = 1
    item_pat_1 = 0
    item_shu_1 = 0
    item_pi_1 = 0
    item_cho_1 = 0
    item_tang_1 = 0
    item_tang_2 = 0
    item_tang_3 = 0
    item_tang_4 = 0
    item_tang_5 = 0
# 여기에서부터 게임이 시작합니다.
label start:
    play music all_song volume 1.0
    show screen inventory_display_toggle
    ac "누구나 사랑하는 사람을 위해\n가슴에 따뜻한 붕어빵을 하나씩 품고 다니는 추운 겨울 날이었다… "
    ac "나는 어린 시절 살았던 동네로 다시 이사를 오게 되었고, 드디어 첫 등교날..."

    $ pname = renpy.input("내 이름은?")

label firstchater:
    scene bg_class_1
    show c_boong :
        xpos 320
        ypos -200
    boong "자, 오늘은 새로운 전학생이 왔어요~"
    boong "전학생 친구? 자기 소개 한 번 해볼까요?"
    
    hide c_boong

    menu: #자리선택
  
        "안녕, 난 [pname]이야. 잘 부탁해." :
            
            $ chooseTang = 1
            show c_boong:
                xpos 320
                ypos -200
            boong "아, 그래. 저쪽에 자리가 비었구나."
            boong "이제부터 저 곳이 너의 자리가 될 거야."
            ac "나는 비어있는 자리에 앉았다." 
            #$ inventory_items.append("초콜릿")
            #$ inventory_items.append("탕후루")
            jump selection1_1

        "안녕, 난 [pname]이야. 난 팥붕을 좋아해." :
            $ chooseTang = 0
            show c_boong:
                xpos 320
                ypos -200
            boong "팥붕을 좋아하는 친구로구나!"
            boong "아, 그래. 소담이 옆자리가 비었구나."
            boong "이제부터 저 곳이 너의 자리가 될 거야."
            hide c_boong

            ac "나는 팥색 머리를 가진 학생의 옆자리에 앉았다."

            show c_pat_n at p_center
            pat "안녕, 난 박소단이라고 해."
            pat "아까 선생님이 학교 안내를 나한테 부탁하셨어."
            pat "이따 조례 끝나고 나랑 같이 가자."
            #$ item_pat = 1
            #$ inventory_items.append("팥")
            jump selection1_2

        "안녕, 난 [pname]이야. 난 슈붕을 좋아해." :
            $ chooseTang = 0
            show c_boong:
                xpos 320
                ypos -200
            boong "슈붕을 좋아하는 친구로구나!"
            boong "아, 그래. 수림이 옆자리가 비었구나."
            boong "이제부터 저 곳이 너의 자리가 될 거야."
            hide c_boong

            ac "「나는 크림색 머리를 가진 학생의 옆자리에 앉았다.」"
            show c_boong:
                xpos 320
                ypos -200            
            boong "오늘 수림이가 전학생을 도와주렴. 친절하게 설명해주려무나!"
            hide c_boong

            show c_shu_n at s_center
            ac "「수림이 선생님의 말에 작게 고개만 끄덕이고는 살짝 웃으며 내게 말을 걸었다.」"
            shu "조례 끝나고 따라와."

            hide c_shu_n
            ac "「나는 고개를 끄덕이고, 조례가 끝나길 기다렸다.」"
            #$ inventory_items.append("슈크림")
            jump selection1_3     

    
    return

#동아리 안내

label selection1_1 : #탕후루
    
    ac "「조례가 끝나고 선생님이 나를 부르셨다.」"

    scene bg_bokdo with fade
    show c_boong:
        xpos 320
        ypos -200
    boong "자~ 이제 동아리 소개를 해줄 건데... 잠시만, 선생님이 지금 좀..."

    boong "아!" 
    ac "「선생님이 내 옆을 지나가던 학생을 갑자기 덥석, 잡았다. 」"
    boong "정제야, 잘 만났다. 네가 이 친구 동아리 소개 좀 해줄래?"
    boong "선생님이 지금 좀 바빠서 말야~"
    hide c_boong

    show c_cho_n at c_center
    cho "......"
    ac "「초코색 머리를 가진 남자아이는 조용히 고개를 끄덕였다. 」"
    ac "「상당히 과묵한 분위기가 느껴진다. 」"
    hide c_cho_n

    show c_boong:
        xpos 320
        ypos -200
    boong "그럼 난 이만, 잘 부탁한다~"
    hide c_boong
    ac "「선생님은 뒤도 안 돌아보고 쌩- 가버리셨고, 이 아이와 단 둘이 남게 되었다. 」"
    hide c_cho_n

    p "아, 저기... 너 이름이 정제, 맞지?"
    show c_cho_n at c_center
    cho "......"
    hide c_cho_n
    ac"(어, 뭐지. 지금 내 말 씹힌 건가...?)"

    p "저기...? 내 말 듣고 있어?"
    show c_cho_n at c_center
    cho "......"
    ac "어색한 정적이 흐른다......"
    p "저... 근데 동아리 소개 해주는 거 맞지?"

    cho "......"
    cho "따라와."
    hide c_cho_n
    ac "「그 한 마디만 툭 던진 뒤 어디론가 빠르게 향했다. 」"
    p "저기 조금만 천천히 가~"
    cho "......"
    p "(음? 속도 좀 맞춰준거 같은데?)"

    ac "「앞서가던 정재가 어느 교실의 문을 열었다. 」"
    scene bg_lid with fade
    show c_pat_n at p_center
    pat "어, 정재선배? 여긴 웬일이에요?"
    pat "[pname]도 같이있네?"
    hide c_pat_n 

    show c_cho_n at c_center
    cho "...붕선생님이 전학생 동아리 소개시켜달라고 부탁하셔서."
    hide c_cho_n

    show c_pat_n at p_center
    pat "아, 그래서~"
    pat "여긴 도서부야!\n나도 여기 부원이고,"
    pat "도서부원이 되면 여기 있는 책들은 대여 기간 없이 볼 수 있어! \n책 분야별로 붕어빵 개론, 붕어빵의 역사… \n그런 책들이 다양하게 있으니까 편하게 보고 싶을 때, 아무 때나 와서 봐도 괜찮아!"
    hide c_pat_n

    p "아 그렇구나..."
    p "근데...선배?!?!"
    p "선배...님 이셨어요?"
    p "(뭐야 내가 반말했을때 왜 말안해줬지??)"

    show c_cho_n at c_center
    cho "...신경안써...가자. \n바로 옆이 디저트 동아리야"
    p "....네 선배님.."
    p "(한층 더 어색해졌다..)"
    p "휴..."
    p "(이 분위기 어쩔거야...)"
    hide c_cho_m

    scene bg_dess with fade
    ac "「한숨을 쉬며 내려다본 바닥에 작은 키링이 떨어져 있었다. 」"

    show c_cho_n at c_center
    p "어? 이건... 초콜릿? 토끼 모양이네..."
    p "아 키링이구나! \n귀여운데 누구가 떨어트린거지?"
    ac "「주위를 둘러보는데 앞서가던 정제가 뒤를 돌아보며 말했다. 」"
    cho "아... 그 키링 내 거야"
    p "아 여기요!! 키링 귀엽네요. 저도 토끼 좋아해요!"
    p "선배도 토끼 좋아하세요?"
    cho "...초콜릿도 좋아해..."
    p "...아 그러시구나, 저도 좋아해요 초콜릿."
    p "귀엽고 토끼도 달콤... 아, 이게 아니라..."
    cho "...단 걸 좋아한다면 디저트 동아리에 입부하는 것도 괜찮아."
    cho "요즘에는 초콜릿 붕어빵 만들기를 하고 있으니까."
    hide c_cho_n

    scene bg_atelier with fade  
    show c_shu_n at s_center
    shu "으 초콜릿냄새..."
    shu "정재선배?"
    shu "선배 초콜릿냄새좀 빼고 들어와 줄래요? \n머리가 아파서..."
    hide c_shu_n

    show c_cho_n at c_center
    cho "....안 나는데"
    hide c_cho_n

    show c_shu_n at s_center
    shu "많이 나요."
    shu "아, 우리반 전학생이랑 있는걸 보아하니 동아리 소개 때문에 온거죠?"
    hide c_shu_n
    
    show c_cho_n at c_center
    cho "응"
    hide c_cho_n

    show c_shu_n at s_center
    shu "뭐, 여긴 말 그대로 미술부야."
    shu "언제나 다양한 작화로 붕어빵 그림을 그리는 동아리지. \n요즘은 인상파 스타일로 붕어빵을 그리는 연습을 하고 있어."
    shu "설명은 이정도면 충분하지?"
    shu "정재선배 다음은 어디로 가요?"
    hide c_shu_n

    scene bg_bokdo with fade

    show c_cho_n at c_center
    cho "......운동부."
    cho "근데 시간이 조금 부족하네."
    cho "운동부는 밖에 운동장 보이지? \n운동부는 날씨가 나쁘지 않으면 주로 운동장에서 연습해."
    cho "체육관에 있는 모든 스포츠용품은 사용할 수 있는 걸로 알고 있어."
    cho "이제 난 간다."
    cho "입부를 희망하는 동아리가 생기면 붕선생님을 찾아가."
    hide c_cho_n

    ac "「정재가 떠나고 혼자 고민하는 [pname].」"
    
    menu:
        "도서동아리에 들어가야겠어!":
            p "소단이랑 같은 동아리하면 재밌을거같아!!"
            jump selection2_1
        "미술동아리가 들어가야겠어!":
            p "나는 붕어빵 추상화를 그려볼거야!"
            jump selection2_2
        "디저트동아리에 들어가야겠어!":
            p "역시 단게 최고지!"
            jump selection2_1
        "운동동아리에 들어가야겠어!":
            p "체력을 기르겠어!"
            jump selection2_2
    return
            

label selection1_2 : #팥붕

    scene bg_bokdo with fade
    show c_pat_n at p_center
    pat "음, 선생님이 아까 네가 동아리 가입해야 한다고 하셔서, \n동아리를 설명해 주라고 하셨거든?"
    pat "우선은 내가 들어간 도서 동아리가 있어!"
    #장면 전환
    scene bg_lid with fade 
    show c_pat_n at p_center
    pat "도서부원이 되면 여기 있는 책들은 대여 기간 없이 볼 수 있어! \n책 분야별로 붕어빵 개론, 붕어빵의 역사…"
    pat "그런 책들이 다양하게 있으니까 편하게 보고 싶을 때, 아무 때나 와서 봐도 괜찮아!"
    pat "다음은 미술부로 갈게!"

    #장면 전환

    pat "여기가 미술부야! 여기… 어라? \n수림이 있었구나?"
    hide c_pat_n

    scene bg_atelier with fade
    show c_shu_n at s_center
    shu "음?"
    shu "아, 우리 1학년 회장님이 오셨구나 \n동아리 소개 때문에 온 거야?"
    hide c_shu_n

    show c_pat_n at p_center
    pat "응, 맞아! 그래서 말인데, 혹시 간단하게 동아리 소개 한 번만 해줄 수 있어?"
    hide c_pat_n

    show c_shu_n at s_center
    shu "흠… 그래, 그 정도야 뭐, 여긴 말 그대로 미술부야. \n언제나 다양한 작화로 붕어빵 그림을 그리는 동아리지. "
    shu "요즘은 인상파 스타일로 붕어빵을 그리는 연습을 하고 있어."
    shu "그림을 못 그려도 누구나 들어올 수 있으니까 부담 갖지 않아도 괜찮아." 
    shu "이 이 정도면 될까?"
    hide c_shu_n

    show c_pat_n at p_center
    pat "응, 고마워 수림아! 이따 봐! \n좋아, 그러면 다음은 디저트 동아리로 가자!"

    #장면 전환

    scene bg_dess with fade
    show c_pat_n at p_center
    pat "자, 여기가 디저트 동아리야! \n정제 선배가 있으려나?"
    hide c_pat_n
    ac "「뭔가 발에 걸렸다.」"
    p "이건… 초코 색 토끼 키링…?"
    ac "「귀엽다고 생각하는 찰나, 누군가 내 어깨를 톡톡 치는 느낌에 뒤를 돌아봤다.」"

    show c_cho_n at c_center
    cho "… 그거, 내 거야."
    hide c_cho_n

    ac "「손을 뻗길래 놀라지 않은 척 키링을 돌려줬다.」"
    p "(얼굴에 대놓고 비명을 지를 뻔한 걸 겨우 참았네.)"
    p "(인기척이 전혀 느껴지지 않았는데, 도대체 언제 온 거지?)"

    show c_pat_n at p_center
    pat "정제 선배! 계셔서 다행이에요!"
    pat "혹시 잠깐 괜찮으시면 동아리 소개 한 번만 해주시겠어요? \n오늘 전학생이 왔거든요!"
    hide c_pat_n

    show c_cho_n at c_center
    cho "… (한숨) 디저트 동아리야. 붕어빵을 만들기 위한 최적의 레시피를 찾고 있어."
    cho "… 끝."
    hide c_cho_n

    show c_pat_n at p_center
    pat "감사합니다. 선배님!"
    pat "우리 학교 디저트 동아리는 굉장히 유명한데, \n특히 정제 선배가 에이스라고 불리고 있어!"
    pat "같은 동아리면 선배의 붕어빵을 자주 먹어볼 수 있겠지~ 부럽다…"
    pat "다음 동아리로 가보자!"

    #장면 전환

    scene bg_bokdo with fade
    show c_pat_n at p_center
    pat "운동부도 설명해달라고 하고 싶지만, 시간이 별로 없어서 여기서 설명해 줄게."
    ac "(시간이 별로 없긴 한 것 같다.)"
    pat "밖에 운동장 보이지? \n운동부는 날씨가 나쁘지 않으면 주로 운동장에서 연습해!"
    pat "체육관에 있는 모든 스포츠용품은 사용할 수 있는 걸로 알고 있어."
    pat "이정도면 설명이 됐을까? \n곧 수업 시작할 것 같으니까 이제 돌아가자!"
    
    pat "어땠어? 혹시 들어가고 싶은 동아리는 정했어?"
    
    menu :
        "도서 동아리에 들어가고 싶어."  :
            pat "정말?! \n너무 기쁘다! 도서 동아리를 골라줘서 고마워!"
            pat "선생님께 찾아가서 도서 동아리에 들어 가겠다고 얘기 하면 돼!"
            jump selection2_1

        "미술 동아리에 들어가고 싶어."  :
            pat "미술 동아리구나! 같은 반에 있는 수림이도 있으니까 적응하기 쉬울 거야! \n선생님께 찾아가서 미술 동아리에 들어 가겠다고 얘기 하면 돼!"
            jump selection2_2

        "디저트 동아리에 들어가고 싶어." :
            pat "디저트 동아리구나! 정제 선배는 친절하시니까 적응하기 어렵진 않을 거야!"
            jump selection2_3

        "운동 동아리에 들어가고 싶어."  :
            pat "운동 동아리구나! 운동 좋아하면 아주 재미있을거야."
            jump selection2_4

    return

# 행동 「 」, 생각 ()

label selection1_3 : #슈붕(유수림)

    scene bg_bokdo with fade
    show c_shu_n at s_center
    shu "아, 따라왔구나. \n솔직히 네가 혼자 돌아다니면서 물어봐도 될 것 같지만… "
    shu "음… 우선은 소단이를 따라가서 도서부 소개해달라고 할까?"
    ac "「딱히 내 대답을 듣지도 않고, 소단이라는 학생을 따라갔다.」"
    ac "「소단이라는 친구는 기쁜 듯 보인다.」"       #복도 유지
    hide c_shu_n
    
    scene bg_lid with fade
    show c_pat_n at p_center
    pat "도서부에 대해서 내가 알려줄게, 우리 동아리는 붕어빵에 관한 책이 굉장히 많아서 원하는 내용은 거의 다 찾아볼 수 있어! "
    pat "붕어빵 개론, 붕어빵의 역사 등 다양한 책이 있지! "
    pat "도서부에 들어오면 언제든지 그런 책을 볼 수 있으니까 좋아! \n들어오고 싶으면 수림이한테 얘기해줘, 난 책 반납하러 다녀올게!"
    hide c_pat_n
    #팥붕 감

    scene bg_atelier with fade 
    show c_shu_n at s_center
    shu "도서부는 끝났고… 미술부 설명은 내가 해줄게."
    shu "미술부에서는 언제나 다양한 작화로 붕어빵을 그리는 법을 연구하는 동아리야."
    shu "언제나 다양한 작화로 붕어빵 그림을 그리는 동아리지. \n요즘은 인상파 스타일로 붕어빵을 그리는 연습을 하고 있어."
    shu "그림을 못 그려도 누구나 들어올 수 있으니까 부담 갖지 않아도 괜찮아."
    shu "미술부는 이 정도로 하고, 다음은 디저트 동아리로 가자."

    scene bg_dess with fade  
    show c_shu_n at s_center
    shu "여기가 디저트 동아리. \n여긴 누구한테 설명해달라고 할까..."
    hide c_shu_n
    ac "「뭔가 발에 걸렸다.」"
    p "이건… 초코색 토끼 키링…?"
    ac "「귀엽다고 생각하는 찰나, 누군가 내 어깨를 톡톡 치는 느낌에 뒤를 돌아봤다.」"

    show c_cho_n at c_center
    cho "… \n그거, 내꺼야."
    hide c_cho_n

    ac "「손을 뻗길래 놀라지 않은 척 키링을 돌려줬다.」"
    p "(얼굴에 대놓고 비명을 지를 뻔한 걸 겨우 참았네.)"
    p "(인기척이 전혀 느껴지지 않았는데, 도대체 언제 온 거지?)"

    show c_shu_n at s_center
    shu "아, 정제 선배가 있었구나, 다행이네요."
    shu "선배네 동아리, 설명 한 번만 해주시겠어요? \n얘, 전학생이거든요."
    hide c_shu_n

    show c_cho_n at c_center
    cho "… (한숨) 디저트 동아리야. 붕어빵을 만들기 위한 최적의 레시피를 찾고 있어."
    cho "… 끝."
    cho "네가 설명 할 수 있는 건 네가 하지 그래?"
    hide c_cho_n

    show c_shu_n at s_center
    shu "디저트 동아리가 우리 학교에서 가장 유명하다고 해. \n정제 선배가 제일 맛있게 한다고 하지만…"
    shu "글쎄… 미슐랭도 아닌데 그렇게 맛있는지 난 잘 모르겠더라. \n어쨌든, 여기가 디저트 동아리. "
    shu "다음은 운동 동아리인데 곧 수업 시작하니까 돌아가면서 얘기해줄게."
    p "(곧? 아직 시간이 많은 것 같은데…)"

    #장면 전환
    scene bg_bokdo with fade
    show c_shu_n at s_center
    shu "운동 동아리는 체육관이랑 운동장에서 활동해. \n스포츠용품은 다 쓸 수 있는 걸로 알고 있어."
    shu "비가 오거나 눈이 오지 않는 이상 운동장에서 연습하더라. "
    shu "여기까지 설명은 끝내도록 할게."
    shu "이제 들어가고 싶은 동아리는 정했겠지?"
    
    menu:
        "도서 동아리에 들어가고 싶어.":
            shu "도서 동아리라, 그래. 잘 해봐."
            jump selection2_1

        "미술 동아리에 들어가고 싶어.":
            shu "미술 동아리? 다른 동아리도 많은데… 음, 알았어"
            jump selection2_2 

        "디저트 동아리에 들어가고 싶어.":
            shu "디저트 동아리에 들어가고 싶다고? 흠… 그래, 뭐. 가서 잘 해보라고."
            jump selection2_3

        "운동 동아리에 들어가고 싶어.":
            shu "그래? 체력도 중요하긴 하지."
            jump selection2_4
    return


label selection2_1 :
    scene bg_boong with fade
    show c_boong :
        xpos 320
        ypos -200
    ac "「수업이 끝난 후 교무실로 간다. 」"
    boong "오 [pname]이 왔구나."
    p "네 선생님 동아리 입부를 신청하려고 왔어요"
    boong "마음에 드는 동아리는 있었니?"
    p "네!! 저는  도서부에 가입하기로 결정했어요"
    boong "오 좋은 선택이구나 넌 아마 잘 할거같구나. "
    boong "그 동아리는 12월말에 하는 축제에서 매년인기가 많은 동아리 중 하나지, 시험 끝나고 축제 준비하려면 바쁘겠구나"
    p "오 축제..재밌겠네요…가 아니라 시험이요? "
    boong "아 [pname]이는 이제 막 전학와서 좀 정신이 없었나 보구나 2주뒤에 기말고사 란다^^"
    hide c_boong
    p "(아 망했다….)"
    jump pi_appear

label selection2_2 :
    scene bg_boong with fade
    show c_boong :
        xpos 320
        ypos -200
    ac "「수업이 끝난 후 교무실로 간다. 」"
    boong "오 [pname]이 왔구나."
    p "네 선생님 동아리 입부를 신청하려고 왔어요"
    boong "마음에 드는 동아리는 있었니?"
    p "네!! 저는  미술부에 가입하기로 결정했어요"
    boong "오 좋은 선택이구나 넌 아마 잘 할거같구나. "
    boong "그 동아리는 12월말에 하는 축제에서 매년인기가 많은 동아리 중 하나지, 시험 끝나고 축제 준비하려면 바쁘겠구나"
    p "오 축제..재밌겠네요…가 아니라 시험이요? "
    boong "아 [pname]이는 이제 막 전학와서 좀 정신이 없었나 보구나 2주뒤에 기말고사 란다^^"
    hide c_boong
    p "(아 망했다….)"
    jump pi_appear

label selection2_3 :
    scene bg_boong with fade
    show c_boong :
        xpos 320
        ypos -200
    ac "「수업이 끝난 후 교무실로 간다. 」"
    boong "오 [pname]이 왔구나."
    p "네 선생님 동아리 입부를 신청하려고 왔어요"
    boong "마음에 드는 동아리는 있었니?"
    p "네!! 저는  디저트부에 가입하기로 결정했어요"
    boong "오 좋은 선택이구나 넌 아마 잘 할거같구나. "
    boong "그 동아리는 12월말에 하는 축제에서 매년인기가 많은 동아리 중 하나지, 시험 끝나고 축제 준비하려면 바쁘겠구나"
    p "오 축제..재밌겠네요…가 아니라 시험이요? "
    boong "아 [pname]이는 이제 막 전학와서 좀 정신이 없었나 보구나 2주뒤에 기말고사 란다^^"
    hide c_boong
    p "(아 망했다….)"
    jump pi_appear

label selection2_4 :
    scene bg_boong with fade
    show c_boong :
        xpos 320
        ypos -200
    ac "「수업이 끝난 후 교무실로 간다. 」"
    boong "오 [pname]이 왔구나."
    p "네, 선생님. 동아리 입부를 신청하려고 왔어요."
    boong "마음에 드는 동아리는 있었니?"
    p "네!! 저는  운동부에 가입하기로 결정했어요."
    boong "오 좋은 선택이구나. 넌 아마 잘할 거 같구나. "
    boong "그 동아리는 12월 말에 하는 축제에서 매년 인기가 많은 동아리 중 하나지, \n시험 끝나고 축제 준비하려면 바쁘겠구나."
    p "오 축제... 재밌겠네요...가 아니라 시험이요? "
    boong "아 [pname]이는 이제 막 전학와서 좀 정신이 없었나 보구나. 2주 뒤에 기말고사 란다^^"
    hide c_boong
    p "(아  망했다…)"
    jump pi_appear

label pi_appear :
    #<피붕 등장!>

    #하굣길로 페이드인
    scene bg_mstreet with fade
    p "믿기지 않아, 시험기간이라니... 수업에 따라가기 너무 힘들어!!"
    ac "「첫 날이 겨우 끝나고, 드디어 하교를 하게 되었다.」"
    ac "「이 근처에는 내가 어렸을 때 자주 가던 붕어빵 집이 한 군데가 있다.」"
    ac "「아까 등교하는 길에 슬쩍 봤는데, 아직도 남아 있다는 사실에 기뻤다.」"
    ac "「왜냐하면 여기는...」"
    ac "「이 동네에서 유일하게 피자맛 붕어빵을 파는 곳이기 때문이다!」"

#붕빵집

    p "(드디어 붕어빵 집에 도착했다! 남아 있는 피붕은 단 두 개…)"
    p "(설마 앞에 있는 사람이 다 사가지는 않겠지?)"

    show c_pi_n at pi_center
    pi "피자 붕어빵 두 개 주세요."
    hide c_pi_n

    p "(?!)"
    p "(지금 피자 붕어빵 두 개를 다 산 거야?)"
    ac "「눈을 깜빡이며 믿을 수 없다는 듯이 저… 빨간머리 남학생을 봤다.」"
    p "(교복이 우리 학교 옷 같은데, 설마 같은 학교인 건가?)"
    p "(안 돼, 내 어릴 적 추억이 담긴 피붕을…! 여기서 물러설 순 없어...! 이판사판이다!)"

    p "저기, 혹시 붕빵고 학생 맞아?"
    show c_pi_n at pi_center
    pi "하? 지금 그걸 몰라서 묻는 거야?"
    p "그럼 그, 혹시 그 피자 붕어빵… 나한테 하나만 줄 수 있을까?"
    p "아니, 내가 돈 줄게. 나한테 팔아줘 제발!"
    pi "…뭐?"
    #속사포 하는 느낌으로 효과 줍시다.
    p "난 이상한 사람이 아니라 내가 이사 가기 전에, 진짜 옛날에 이 집에서 먹었던 피자 붕어빵 맛을 잊지 못해서 다시 먹으러 이사 온 거거든? 오늘 전학도 와서 첫 등교란 말야! 제발 오늘 하루를 피자 붕어빵으로 마무리 할 수 있게 해줘!"
    "....." 
    pi "흠......"
    ac "「잠시 고민하는 듯 보인다.」"
    pi "네 녀석, 합격이다."
    p "응? 합격?"
    pi "그래, 합격. 피자 붕어빵에 대한 열정이 제법이잖냐, 너?"
    p "저, 정말..? 그럼 나 하나 주는 거야? 잠깐, 돈 바로 꺼낼게…!"
    pi "돈은 안 줘도 괜찮아, 피자 붕어빵 동지를 만난 기념으로 그냥 하나 줄게."
    hide c_pi_n

    menu pi_selection1 :#<선택지>
        "와, 진짜?! 정말 고마워! 잘 먹을게!" :
            show c_pi_n at pi_center
            pi "어, 맛있게 먹으라고 전학생."
            #(1개)

        "너, 정말 좋은 녀석이구나…! \n다음엔 내가 꼭 사줄게! 진짜 진짜 고마워!" :
            show c_pi_h at pi_center
            ac "「도하의 얼굴이 붉어졌다.」"
            pi "흐,흥! 딱히 네가 좋아서 주는 건 아니거든…?!"
            pi "마, 맛있게 먹던가 말던가… 안 사줘도 돼!"
            #(2개)

        "뭐야, 필요 없는 거 였으면 애초에 하나만 샀으면 됐잖아!" :
            show c_pi_m at pi_center
            pi "아앙? 네 놈 지금 뭐라고 했냐?"    
            #<<게임 오버>>
            jump gameover

    show c_pi_n at pi_center
    pi "그럼 나는 이만 갈게."
    pi "아, 그리고, 내 이름은 전도하니까. 기억해둬라."
    pi "그럼 또 보자."
    p "아앗, 저기이--!!"
    hide c_pi_n
    hide c_pi_h

    ac "「도하라던 애는 그러곤 쏠랑 사라져버렸다.」"
    p "(그냥 가버렸네... 나중에 만나면 꼭 보답해줘야겠다.)"
    ac "「나는 공짜 피자 붕어빵을 안고, 신나게 집으로 향했다.」"
    ac "「그덕에 시험에 대한 걱정은 잊어버리고 말았다.」"

#페이드 아웃
#페이드 인 <교실>

label selection3 :
    scene bg_class_1 with fade
    p "(어제 피자 붕어빵 먹느라 시험 생각을 못했잖아...! 어떡하지...?)"
    p "하아......"

    show c_pat_n at p_center
    pat "[pname]아, 무슨 일 있어?"
    p "어? 소단아, 그게... 난 붕어빵에 대해서 아는 게 하나도 없는데 2주 뒤에 시험이래!"
    p "나 어쩌지......"
    pat "아, 시험공부 때문에 그랬구나. 가장 걱정되는 과목이 뭔데?"
    hide c_pat_n

    menu selection3_1 :
        "붕어빵의 역사" : #팥루트
            jump pat_study1

        "붕어빵 심리학" : #슈루트
            jump shu_study1

        "붕어빵 재료 공학" : #피자루트
            jump pi_study1

        "붕어빵 제조 실습" : #초코루트
            jump cho_study1

label pat_study1 :
    show c_pat_n at p_center
    p "난 역시 붕어빵의 역사가 가장 어려운 거 같아..."
    pat "아, 그건 내가 전문이지. 내가 도와줄게."
    hide c_pat_n

    menu pat_selection1 :
        "응, 그래. 좋아~" : #팥 1개
            show c_pat_n at p_center
            pat "그럼 시작해볼까?"
            jump pat_study2

        "너 혼자 공부하기도 바쁠 텐데, 도와준다고 해서 정말 고마워. \n더 힘내서 공부할 수 있을 거 같아. 열심히 해볼게!" : #팥 2개
            show c_pat_h at p_center
            pat "아냐, 나 가르쳐 주는 거 좋아해."
            pat "나도 알려주면서 복습할 수 있고."
            pat "그리고 너랑 같이 공부하게 되니 오히려 좋은 걸."
            jump pat_study2

        "미안한데 요점 정리한 노트만 주면 안 될까?" :
            show c_pat_m at p_center
            pat "어...? 그건 좀... 미안... 다른 애 알아봐."
            jump gameover
    return

#페이드 아웃

label pat_study2 : #페이드 인 <빈 교실>

    scene bg_class_3 with fade
    ac "「소단이와 함께 방과 후 빈 교실에 남아서 공부하기로 했다.」"

    show c_pat_n at p_center
    pat "여기부터 시작해볼게. 붕어빵의 역사는 일본 도미빵에서 유래된 건데......"
    ac "「열심히 설명 중......」"
    pat "이해했어?"
    p "응! 덕분에 공부가 좀 더 수월해질 거 같아! 고마워."
    pat "그래, 도움이 됐다니 다행이다."
    pat "이제부턴 각자 공부 하자."
    pat "궁금한 거 있으면 뭐든 물어봐 \n내가 알려줄 수 있는 건 최대한 알려 줄게"
    p "응, 알겠어!"
    hide c_pat_n

    ac "「공부 중......」"
    ac "「열심히 공부를 하다가도 왠지 모르게 소단이에게 눈길이 갔다.」"
    p "(공부에 열중하는 모습이... 멋있는 걸.)"
    p "(무엇보다 손이 정말 예쁘다...)"

    show c_pat_n at p_center
    pat "집중 안 하고 뭐 해, [pname]아."
    p "(헉! 너무 뚫어져라 쳐다본 걸까?)"
    p "(아니 그것보다, 지금 얼굴이 너무 가깝지 않아?!?!)"
    p "아니, 그, 그게! 구,궁금한 게 있어서!"
    pat "그래? 진작에 물어보지, 뭔데?"
    p "이 문제가 좀 어렵네...!"
    pat "아, 이거는 이런 식으로 생각하면 쉬워......"
    pat "이렇게, 저렇게... 풀면 돼."
    pat "어때, 이제 이해가 좀 돼?"
    hide c_pat_n

    menu pat_selection2 :
        "응, 너 설명 정말 잘 한다~ 재능 있는데?" : #팥 1개
            show c_pat_n at p_center
            pat "하하, 별 거 아니야."
            jump pat_study3

        "응, 이해했어! 이렇게 쉽게 설명해주다니, \n너 정말 공부 잘하는 구나?" : #팥 2개
            show c_pat_h at p_center
            pat "그렇게 말 해주니까 좀 쑥스럽네, 고마워."
            jump pat_study3

        "아 너무 어려워!! 못 해 먹겠다! 그만하면 안 될까?" : #게임 오버
            show c_pat_m at p_center
            pat "[pname]는 끈기가 부족하구나…"
            jump gameover
   
    return

label pat_study3 :
    scene bg_class_3 with fade
    show c_pat_n at p_center
    pat "이제 됐지? 모르는 거 생기면 또 물어봐."
    p "응, 고마워."
    p "(아까부터 느낀 거지만 소단이는 웃는 게 참 예쁘네.)"
    p "(나도 덩달아 미소 짓게 만들어!)"
    p "(다시 보니 잘 생긴 거 같기도 하고......)"
    p "(아니아니! 내가 지금 무슨 생각을!!!)"
    p "(정신 차리자! 공부에 집중하라구 [pname]!!!)"
    hide c_pat_n
    ac "「다시 공부 모드......」"

    scene bg_nclass_1 with fade
    p "(시간이 얼마나 흘렀을까...? 슬슬 졸리기 시작하네...)"
    ac "「나도 모르게 고개가 아래로 푹푹 떨어졌다.」"
    ac "「꿈뻑 꿈뻑......」"

    show c_pat_n at p_center
    pat "[pname]아, 많이 졸려?"
    ac "「!!!!!!!!」" with vpunch
    ac "「날 부르는 목소리에 눈을 떠보니, 소단이의 얼굴이 보였다.」"
    p "어, 어! 미안!!!! 졸아버렸네, 하하..."
    pat "놀래킬 생각은 없었는데, 미안."
    pat "근데 너 얼굴이 많이 빨간데, 어디 아픈 거야?"
    ac "「대뜸 내 볼에 손을 대는 소단이 때문에 얼굴이 더 붉어질 것만 같았다.」"
    p "아, 아니, 그게 아니고..."
    p "(네 얼굴이 가까워서 그렇다고 어떻게 말해...)"
    p "(조금만 떨어져 주란 말야!)"
    p "그냥 조금 더워서... 하하."
    ac "「어색함에 나도 모르게 고개를 홱 돌려버렸다.」"
    pat "많이 졸려 보이는데, 이제 그만 집에 갈까?"
    pat "공부는 억지로 하면 더 안 되거든."
    p "그, 그래. 그게 낫겠다...!"

    #페이드 아웃
    #페이드 인 <하굣길>

    scene bg_nstreet with fade
    show c_pat_n at p_center
    pat "오늘 정말 수고 많았어. 피곤하지?"
    p "조금 피곤하긴 한데, 너랑 같이 하니까 좋았어."
    p "진짜 고마워, 소단아."
    pat "걱정 많았는데, 좋았다니 다행이네."
    pat "근데 혹시 집이 어느 쪽이야? 데려다줄까?"
    hide c_pat_n

    menu pat_selection3 :
        "아니, 괜찮아. 나 혼자 가도 돼." : #게임 오버
            show c_pat_m at p_center
            pat "아... 그래... 잘 가..."
            jump gameover

        "아, 난 이쪽으로 가." : #팥 1개
            show c_pat_n at p_center
            pat "아... 나랑 반대 방향이네."
            pat "아쉬운데 근처까지만이라도 데려다줄게."
            p "아 그럼, 붕어빵 편의점 앞까지만 데려다줄래?"
            jump pat_study4

        "응, 조금 무서운데... 데려다줄래?" : #팥 2개
            $ item_boong = 2
            $ item_pat_1 = 1
   
            show pat_1 at pat_1_center
            "팥소 한 개를 얻었다!\n3개를 모으면 팥 붕어빵을 만들 수 있다"
            hide pat_1
            show c_pat_h at p_center
            ac "「소단이가 활짝 웃는다.」"
            pat "그래, 어디로 가면 돼?"
            p "붕어빵 편의점 근처인데 그 앞까지만 같이 가줘!"
            
            jump pat_study4
   
    return

label pat_study4 :
    show c_pat_n at p_center
    pat "그래, 가자."
    ac "「그 순간 소단이가 살며시 내 손을 잡았다.」"
    p "어...?"
    show c_pat_h at p_center
    pat "이러고 가도 괜찮지? 손 시렵잖아, 하하..." #얼굴 발그레한 사진 꼭 넣어주십쇼.
    p "아... 으응... 조, 좋아..."

    hide c_pat_n
    hide c_pat_h
    ac "「손을 잡고 가면서 왠지 모르게 마음이 싱숭생숭했다.」"
    ac "「소단이 때문인 걸까...? 나도 내 맘을 잘 모르겠다...」"
    ac "「우린 가면서 아무 말도 하지 못했다.」"
    ac "「그러다 보니, 어느새 목적지에 도착해버리고 말았다.」"

    show c_pat_n at p_center
    pat "다왔다...... 조심히 들어가."
    p "응! 소단이 너도! 내일 학교에서 봐!"
    ac "「난 부끄러움에 뒤도 안 돌아보고 집으로 도망쳤다.」"
    if chooseTang == 1 :
        $ item_boong = 2
        $ item_pat_1 = 2
        $ item_shu_1 = 2
        $ item_cho_1 = 2
        $ item_pi_1 = 2
        $ item_tang_2 = 1
        jump testTangAppear

    elif chooseTang == 0 :
        jump test


#페이드 아웃

label shu_study1 :
    scene bg_class_1 with fade
    p "난 역시 붕어빵 심리학이 가장 어려운 것 같아... \n심오해서 이해하기 어렵달까..."

    show c_pat_n at p_center
    pat "아, 심리학 좀 어렵지... 나도 그 과목은 좀 어려워해서..."
    pat "붕어빵 심리학은 관찰력이 뛰어난 사람이 잘하는 것 같아"
    p "내가 눈치 없단 소리는 자주 듣긴 하지..."
    hide c_pat_n

    show c_shu_n at s_center
    shu "너네 무슨 얘길 그렇게 해?"
    hide c_shu_n

    show c_pat_n at p_center
    pat "아, [pname]이가 붕어빵 심리학 공부가 힘들다 해서 말야."
    hide c_pat_n

    show c_shu_n at s_center
    shu "그런가. 제일 쉽지 않아?."
    hide c_shu_n
    
    menu shu_selection1 :
        "나는 심리학이 제일 어렵던데... 네가 나 좀 도와주면 안 될까? \n제발 부탁이야!!" :
            show c_shu_n at s_center
            shu "흠, 어디서 하든지 상관없다면야... 도와줄게."
            p "(왜 불안하지...?)"
            p "으응...!! 고마워, 하핫!"
            jump shu_study2
       
        "와, 너 관찰력이 좋은가보다... \n부러워! 나는 이 과목이 제일 어려운데..." :
            show c_shu_n at s_center
            shu "하하, 원한다면 공부 좀 도와줄까?"
            p "와, 정말? 너무 고마워!"
            hide c_shu_n
            show c_shu_h at s_center
            shu "이 정도로 뭘, 그럼 토요일에 학교 앞에서 보자."
            hide c_shu_h
            jump shu_study2
       
        "... 너 내가 멍청하다는 뜻이니?!" : #게임오버
            show c_shu_m at s_center
            shu "...그런 생각 안 하고 있었는데 갑자기 좀 드네."
            jump gameover


#페이드 아웃




label shu_study2 : #페이드 인 <학교 앞(야외)>
    scene bg_mstreet with fade
    p "(근데 왜 주말에 학교 앞에서 보자고 한 걸까.)"
    p "근처에 아는 장소가 있나?"
    ac "「골목에서 누군가와 함께 있는 유수림의 뒷모습을 발견했다.」"
    p "어, 저기 저 사람 수림이 아닌가?"
    p "근데 누구랑 같이 있네? 무슨 일이지?"
    ac "「조금 더 가까이 다가가자, 두 사람의 대화가 희미하게 들린다.」"

    show c_shu_n at s_center
    shu "아, 정말 미안해. 난 지금 연애할 생각이 없어서."
    hide c_shu_n
    
    p "(와, 수림이 고백 받았나봐. 정말 인기가 많네...)"
    p "(앗, 저 여자애 선물까지 준비했네.)"
    ac "「고백한 여자애는 도망가고 골목에는 수림이만 남았다.」"
    p "(본의 아니게 이런 걸 들어 버렸네... 수림이한테 미안하다고 해야겠다.)"
    p "저기, 수림..."

    show c_shu_m at s_center
    shu "쯧, 귀찮게..."
    ac "「수림은 귀찮은 듯이 선물을 바닥에 버렸다.」"
    hide c_shu_m

    p "아앗, 이쪽으로 온다!!!"
    ac "「나는 급하게 그 자리를 피했다.」"
    p "방금 내가 뭘 본 거지...?"
    ac "「그 때 누군가가 내 어깨를 두드렸다.」"
    p "깜짝이야!!"

    show c_shu_n at s_center
    shu "일찍 왔네? 근데 죄 지은 사람처럼 왜 이렇게 놀라?"
    p "아, 아니야. 좀 뛰어 왔더니..."
    shu "그래? 뛰어올 필요는 없었는데."
    shu "어쨌든, 이제 가자."
    p "어디로?"
    shu "나 이 근처에 살아, 우리 집으로 가자."
    p "어어? 갑자기?!?"

#화면 전환 <유수림의 집>
    scene bg_shuroom with fade
    show c_shu_n at s_center
    shu "여기가 내 집이야. 편하게 들어와도 좋아."
    p "실례합니다아... "
    p "와, 너희 집 엄청 좋다~"
    p "(갑작스럽게 수림이 집에 오게 되다니... 약간 불편한 걸...)"
    shu "참고로 집엔 아무도 없어. 나 혼자 살 거든."
    p "정말? 너 나랑 동갑 맞지? 언제부터?"
    shu "부모님이 이혼하셔서. 그니까 편하게 있어."
    p "(한층 더 불편해졌다… 안 그래도 아침에 있었던 일 때문에 불편한데 집에서도 둘이서만 있어야 한다니…) "
    shu "여기가 내 방이야. 앉아 있으면 마실 거라도 가져다줄게."
    hide c_shu_n
    ac "「잠시 후」"
    show c_shu_n at s_center
    shu "미안, 집에 대접할 게 물뿐이네."
    p "아냐, 괜찮아. 고마워, 잘 마실게!"
    shu "그럼 우리 이제 공부할까?"
    shu "먼저 붕어빵 꼬리를 먹는 사람 유형에서 손으로 뜯어먹는 사람과 베어먹는 사람의 심리 차이인데..."
    hide c_shu_n

    p "(아... 집중해야 하는데, 사정 들으니까 자꾸 신경 쓰이네...)"
    p "(수림이 완전 왕자님처럼 생겨서 혼자 사는 구나...)"
    p "(부모님이 이혼하셔서 이런 큰 집에서 혼자 살다니 외롭지 않나...)"
    p "(그래서 아까 전에 고백 받은 게 싫었나...? 그런 거면 조금 불쌍...)"

    show c_shu_n at s_center
    shu "...[pname]아, 듣고 있어?"
    p "아, 미안... 다시 집중할게."
    shu "혹시 아까 부모님이 이혼했다고 해서 그래?"
    hide c_shu_n

    menu shu_selection2 :
        "아니 그게 아니라. 혼자 사는 게 대단한 거 같아서. \n나라면 친구를 집에 초대하기도 힘들었을 거야." : #슈 2개
            p "앗, 기분 나빴다면 정말 미안해!"
            p "그냥 나라면 많이 힘들 것 같아서..."
            ac "「잠시 생각에 빠진 듯하다.」"
            #호감도 상승 이미지
            show c_shu_h at s_center
            shu "아니, 괜찮아. 처음에 좀 외롭긴 했는데, 혼자 산지는 꽤 오래 돼서 적응 됐어."
            shu "집이 조용하니까 그림 연습하는데 도움이 되기도 하고."
            jump shu_study3
       
        "그런 거 아냐! 그냥 너 혼자 살면 심심하겠다 싶어서. 하하..." : #슈 1개
            show c_shu_n at s_center
            shu "뭐야, 싱겁게."
            shu "가끔 좀 심심하긴 하지만 뭐 괜찮아."
            #호감도 상승 이미지
            shu "그림 그리기에는 조용한 게 편하기도 하고."
            jump shu_study3


        "응, 나 이혼가정 처음 봐!!!" : #게임오버
            show c_shu_m
            shu "...그게 신기해?" #경멸
            jump gameover


label shu_study3 :
    scene bg_shuroom with fade
    p "그렇구나... 수림이 너는 미술부도 하고 집에서도 그림 그리는 거야?"
    show c_shu_n at s_center
    shu "응, 동아리는 그냥 학교에서 남는 시간에 그림이나 그리려고 들어 간 거야."
    shu "집에서 그림을 더 많이 그려."
    p "와, 그럼 저기 걸려있는 그림들 다 네가 그린 거야? \n너무 멋있다!"
    p "그림 그리는 거 정말 좋아하나보네? \n좋아하는 일을 잘하는 사람이 나는 너무 부럽더라!"
    p "그리고 손재주 좋은 사람들이 요리도 잘하던데, 너 요리 잘해?"
    shu "나한테 너무 관심이 많은 거 아냐?"
    p "에엣!? 저, 절대 그런 거 아니거든! 오해하지 말아줘!!"
    p "정말! 진짜로! 흑심 있는 거 아니라구!"
    shu "흑심이라고는 안 했는데."
    p "너 정말!!"
    hide c_shu_n

    show c_shu_h at s_center
    shu "하하, 알았어. 그만 놀릴게. 화내지 마."
    p "(앗, 저렇게 웃는 거 처음 보네... 역시 나쁜 애는 아닌 거 같아...)"
    p "아까 있었던 일 한번 물어볼까..."
    p "수림아, 그런데 사실... 나 아까 오전에 골목에서 너 봤어!"
    hide c_shu_h

    menu shu_selection3 :
        "근데 너 좀 쓰레기 같더라." : #게임 오버
            show c_shu_m
            shu "...그 애 스토커야." #경멸
            jump gameover
       
        "혹시 요즘 안 좋은 일 있어?" : #슈 1개
            show c_shu_n at s_center
            shu "역시 봤구나."
            shu "그냥 별일 아니였어. 그런 식의 선물을 싫어해서. "
            p "그래도 선물을 바닥에..."
            shu "네가 주는 건 받을게."
            p "뭐, 뭐라는 거야! 내가 너한테 왜!!!"
            shu "공부 가르쳐준 답례, 안 할거야?"
            p "너 정말!! 그만 놀린다며!!!"
            if chooseTang == 1 :
                
                jump testTangAppear


            elif chooseTang == 0 :
                jump test

        "그냥 숨기기 싫어서... 일부러 본 건 아냐, 미안!" : #슈 2개
            $ item_boong = 2
            $ item_shu_1 = 1
            show shu_1 at shu_1_center
            "슈크림 한 개를 얻었다!\n3개를 모으면 슈크림 붕어빵을 만들 수 있다"
            hide shu_1
            show c_shu_h at s_center
            shu "음, 아니. 괜찮아."
            p "너 혹시... 요즘 힘든 일 있어서 그래?"
            shu "그런 거 아냐. 사실 그 애 스토커거든."
            p "뭐?! 하마터면 오해할 뻔했네, 미안해!"
            shu "별일 아니야 \n사실 오늘 여자친구 만나러 가는 거라고 했는데도 포기를 안 해서."
            p "응? 여자친구? 나, 나 말하는 거야?"
            shu "응, 그럼 떨어져 나갈까 해서."
            shu "그냥 확실하게 너랑 같이 가서 말할까?"
            hide c_shu_h
            ac "「얼굴이 불타듯이 뜨거워졌다.」"
            p "미쳤나봐 정말!!!"
            
            if chooseTang == 1 :
                $ item_boong = 2
                $ item_pat_1 = 2
                $ item_shu_1 = 2
                $ item_cho_1 = 2
                $ item_pi_1 = 2
                $ item_tang_3 = 1
                jump testTangAppear

            elif chooseTang == 0 :
                jump test


label pi_study1 : #<교실>
    hide c_pat_n
    p "난 역시 붕어빵 재료 공학이 가장 어려운 것 같아."
    show c_pat_n at p_center
    pat "아, 그래? 그럼 도하 선배한테 부탁해보는 게 어때?"
    p "어?! 도하 선배? 선배였어?"
    pat "응, 우리보다 한 살 많아."
    p "(뭐야! 동갑인 줄 알았는데 선배였잖아?)"
    p "(아니 선배라고 말을 왜 안 해주는 건데!!!)"
    p "(이 학교 선배들은 선배인 거 다 숨기나?)"
    pat "어때, 그 선배랑 같이 할래?"
    p "아... 음... 그러지 뭐..."
    p "(그 선배 조금 못 미덥긴 한데... 속는셈 치고 해보자...)"
    p "(편견을 가져선 안 되지, 응응...)"
    pat "선배한테 연락해놨어. 학교 끝나고 도서관 앞으로 가면 돼."
    p " 응, 알겠어! 고마워!"


#장면 전환 <도서관 앞> -> 복도 사진 넣으면 될 듯??
    scene bg_bokdo with fade
    ac "「나는 학교 수업이 마치는 대로 도서관 앞으로 갔다.」"
    ac "「기다리고 있는데, 저 멀리서 선배가 오는 게 보였다.」"
    show c_pi_n at pi_center
    pi "어이, 거기 너. 또 보네."
    pi "나한테 붕어빵 재료 공학 가르쳐 달라고 했다면서."
    p "아, 네..."
    pi "그리고 너 1학년이더라? 혼날래?"
    ac "「선배가 갑자기 헤드락을 걸어왔다.」"
    p "아악! 그 땐 죄송했어요! 근데 선배도 말 안 해줬잖아요!"
    ac "「선배는 짖궂게 웃으며 순순히 헤드락을 풀어주었다.」"
    pi "하하, 장난이야, 장난. 그냥 이름 편하게 불러."
    pi "선배, 선배 거리는 건 오글거려서 못 들어주겠더라."
    p "그래, 전도하! 너가 먼저 그렇게 부르라고 했다!"
    p "나중에 딴 말하기 없기."
    pi "하하, 그래, 딴 말 안 해."
    pi "이제 들어가자."
    hide c_pi_n
    ac "「선배는 내 머리를 헝클어트리곤 도서관 안으로 홀랑 들어갔다.」"
    p "아, 같이 가ㅡ!"

#장면 전환 <도서관>
    scene bg_lid with fade
    ac "「도서관 안엔 시험 공부 하는 학생들로 가득했다.」"
    p "(다들 정말 열심이구나...)"
    ac "(근데 생각해보니까 조용히 해야하는 도서관에서 어떻게 가르쳐준다는 거지?)"
    ac "「나는 선배 옆자리에 나란히 앉았다.」"
    ac "「책상에 공부할 책과 필기구를 하나씩 꺼내놓고 있는데...」"
    ac "「옆에서 선배가 무언가 적은 포스트잇을 슬쩍 건넸다.」"
    ac "「대충 흘겨쓴 글씨체 때문에 알아보기 힘들었지만......」"
    ac "「포스트잇에 적혀있는 내용은 이랬다.」"
    ac "「나는 스파르타식이라 하나하나 가르쳐 주지 않아.」"
    ac "「개인적으로 공부하고 모르는 것만 질문할 것!」"
    ac "「이런 쪽지만 덜렁 남겨둔 채, 본인은 그냥 책상에 엎드려 버린다.」"
    p "(아악! 이럴 줄 알았어. 어쩐지 못 미덥더라니. 너무 하잖아!)"
    p "(소단이 이 녀석은 대체 왜 이 선배를 추천해준 거야?)"
    ac "「정말 얄미웠지만 뭐라 대꾸하지도 못 하고, 그냥 혼자서 공부할 수 밖에 없었다......」"
    ac "「시간이 흐르고......」"
    p "(으으ㅡ! 몇 시지? 나도 모르게 열심히 공부했네?)"
    p "(나 그래도 한다면 하는 애잖아?)"
    ac "「몸이 조금 뻐근해 기지개를 키다가 선배 쪽을 슬쩍 봤는데,」"
    show c_pi_n at pi_center
    ac "「선배가 엎드린 채 나를 쳐다보고 있었다.」"
    p "뭐야, 언제부터 보고 있었어?"
    pi "나 심심해."
    p "실컷 잠만 잤으면서 뭔 소리야."
    pi "잠깐만 바람 쐬고 오자, 나와."
    p "아잇, 잠깐! 아직 시험범위까지 한참 남았는데!"
    ac "「내 말은 듣지도 않고 제멋대로 내 팔을 덥썩 잡아 날 이끌었다.」"


#장면 전환 <운동장>
    scene bg_ground with fade
    show c_pi_n at pi_center
    pi "그래도 막상 나오니까 괜찮지?"
    p "응... 좀 낫긴 하네..."
    p "그나저나 우리 어디 가는 건데?"
    pi "피자 붕어빵 먹으러 가자, 내가 또 쏜다."
    p "어, 진짜? 아싸! 이렇게 또 얻어 먹어도 되는 거야?"
    pi "뭐, 딱히 네가 좋아서 사주는 건 아니고,"
    pi "아까 보니까 혼자서도 열심히 하는게 보기 좋아서 사주는 거니까 오해는 말라고!" #얼굴 붉히는 거 넣으면 좋겠삼요.^^
    p "참나, 오해한 적 없거든요!"
    pi "그나저나 내 도움없이도 잘하더라?"
    p "선배 너가 무책임하게 그냥 잤잖아!"
    p "그러니 혼자라도 해내야지 뭐, 어째."
    pi "푸하하, 기특하네, [pname]."
    p "내가 앤 줄 알아!"
    hide c_pi_n
    ac "「그렇게 서로 티격태격 하고 있던 그 순간!」"
    ac "「슈욱ㅡㅡ!」" with vpunch
    #여기 흔들리는 효과? 넣자 -> 넣었다. 하하하하 내가 해냄!
    ac "「어디선가 공이 내 쪽을 향해 날아오고 있었다.」"
    p "꺄악!"
    pi "[pname]!!! 위험해!!!" with vpunch
    ac "「놀란 마음에 두 눈을 꼭 감고 있었는데,」"
    ac "「......」"
    ac "「아무런 느낌이 들지 않았다.」"
    p "(응? 뭐지...? 설마...)"
    ac "「급히 눈을 뜨자, 내 앞을 막고 있는 선배가 보였다.」"
    p "(뭐야, 나 대신 자기가 공에 맞은 거야...?)"
    show c_pi_m at pi_center
    pi "어이, 거기, 너네! 조심해야지! 사람이 다칠 뻔했잖아!"
    pi "[pname], 괜찮아?"
    hide c_pi_m

    menu pi_selection2:
        "으, 응...! 것보다 너 괜찮은 거야...?" : #토마토? 1개
            show c_pi_n at pi_center
            pi "하, 큰일 날 뻔했네. 내가 막아서 망정이지..."
            jump pi_study2
       
        "야, 전도하! 아무리 날 구한다고 해도 그렇지. \n왜 네가 대신 공에 맞고 그래?" : #토마토 2개
            show c_pi_h at pi_center
            pi "어, 어?"
            p "너도 위험할 거란 걸 몰라?"
            pi "야, 꼬맹이. 내 몸은 튼튼해서 이정도는 거뜬해."
            pi "걱정 따위 안 해줘도 되거든?" #얼굴 붉히기 흐흐흐흐흐ㅡ헿헤^^
            p "하여튼 허세나 부리고!"
            p "암튼 그래도 앞으론 몸 함부로 쓰지 않기야!"
            jump pi_study2
       
        "무슨 영화 찍어...? 그깟 공 가지고 생쇼는..." : #게임 오버
            show c_pi_m at pi_center
            pi "나랑 싸우자는 거냐, 네 녀석?" #경멸
            jump gameover


label pi_study2 :
    hide c_pi_h 
    show c_pi_n at pi_center
    pi "조심하라고. 특히 너같은 꼬맹이는 말야."
    pi "아, 이런 건 반사 신경이 좋아야 하는데, \n너 나한테 운동 배울 생각 없냐?"
    p "뭐라는 거야! 방금은 반사 신경 좋아도 못 피했다구!"
    p "됐고, 얼른 피자 붕어빵 먹으러 가자."
    p "또 얼마 없을지도 모르잖아."
    pi "그럼 큰일이지, 내가 먼저 가서 네 것도 다 먹어버려야겠다!"
    p "야야, 그런 게 어딨어! 아까까지만 해도 네가 사준댔잖아!"
    hide c_pi_h
    hide c_pi_n
    ac "우리는 서로 아웅다웅 하면서 붕어빵 집까지 달렸다."
    ac "그 상황이 마냥 싫지만은 않았다. \n오히려 재밌다고 해야하나."
    p "(도하 선배... 그냥 장난꾸러기인 줄만 알았는데, 멋있는 점도 있는 거 같고...)"
    p "(매력있는 사람인 거 같아.)"
    p "(사람을 즐겁게 만드는 힘이 있다니까.)"


#장면 전환 <피자 붕어빵 가게>
    scene bg_mstreet with fade
    show c_pi_n at pi_center
    pi "[pname], 너 체력 기를 필요가 있어. 너무 느린 거 아냐?"
    p "헉, 헉... 네가 너무 빠른 거라니까?"
    pi "푸하하, 얼굴 빨개진 거 봐. 피자 붕어빵 닮은 거 같은데?"
    p "놀리지 마라... 죽을래? 선배라고 안 봐준다!"
    pi "아이고, 무서워라."
    p "됐다, 이따 보자. 피자 붕어빵이나 빨리 사줘."
    p "너 때문에 뛰었더니 배고파졌다고."
    pi "그래, 내가 사주는 거니까 감사히 먹어라."
    p "생색 그만 내시고 빨리 사주시죠!"
    ac "「선배는 피자 붕어빵 네 개를 구매해 두 개를 내 양손에 쥐어주었다.」"
    pi "오늘은 다행히 네 개나 있네."
    p "와아ㅡ! 고마워!!! 잘 먹을게, 히히."
    ac "「선배는 붕어빵을 먹는 내 모습을 보더니 베시시 웃는다.」"
    p "왜 웃어, 혹시 뭐 묻었어?"
    pi "아니, 그냥..."
    ac "「좀 머뭇거리더니 이내 대답을 이었다.」"
    pi "피자 붕어빵 먹을 땐 눈이 반짝이는 거 같아서. \n그게 좀..."
    hide c_pi_n

    show c_pi_h at pi_center
    pi "귀여워 보이네." #얼굴 붉히는 모습 넣기!!!!!!!!!
    hide c_pi_h


    menu pi_selection3 :
        "너... 혹시... 나한테 반한 건 아니지...?" : #게임 오버
            show c_pi_m at pi_center
            pi "아앙? 뭐라는 거냐, 너." #경멸
            jump gameover
         
        "귀, 귀엽다니! 아니거든!" : #토마토(?) 1개
            show c_pi_n at pi_center
            pi "너 얼굴 또 빨개졌다. 부끄러워?"
            p "아, 아니. 안 부끄러워! 추워서 그래!"
            jump pi_study3
       
        "내가 좀 귀엽긴 하지. 근데... 선배 너도 아까 좀 멋있었어...!" : #토마토 2개
            $ item_boong = 2
            $ item_pi_1 = 1
            show pizza_1 at pizza_1_center
            "피자 재로 한 개를 얻었다!\n3개를 모으면 피자 붕어빵을 만들 수 있다"
            hide pizza_1
            show c_pi_h at pi_center
            pi "푸하하, 이런 말도 할 줄 알아? 의왼데?"
            
            #호감도 상승 이미지
            jump pi_study3


label pi_study3 :
    scene bg_mstreet
    show c_pi_n at pi_center
    pi "그나저나 우리 두번째로 만난 건데도 하나도 안 어색하네."
    p "그러게... 오래 본 사이같이 편해."
    pi "네가 사람을 좀, 편하게 해주는 거 같아."
    p "그런가...?"
    pi "혹시... 내일 또 만날래?"
    pi "내일은... 공부 제대로 가르쳐 줄게."
    p "그, 그러든지. 내일은 진짜 가르쳐 줘야 된다?"
    pi "스파르타식으로 달릴 거니까 각오하는 게 좋을 걸."
   
    hide c_pi_n
    ac "「그렇게 우리는 다음을 기약했다.」"
    ac "「피자 붕어빵을 다 먹고나서도 그 추운 겨울에 밖에서 신나게 떠들었다.」"
    ac "「덕분에 공부는 못 했지만......」"
    ac "「그래도 즐거운 추억으로 남을 듯 하다.」"
#페이드 아웃
    if chooseTang == 1 :
        $ item_boong = 2
        $ item_pat_1 = 2
        $ item_shu_1 = 2
        $ item_cho_1 = 2
        $ item_pi_1 = 2
        $ item_tang_4 = 1
        jump testTangAppear


    elif chooseTang == 0 :
        jump test


label cho_study1 : #<교실>
    scene bg_class_1
    p "난 역시 붕어빵 제조 실습이 가장 어려운 것 같아."
    show c_pat_n at p_center
    pat "아, 그래? 그럼 정제 선배한테 부탁해보는 게 어때?"
    pat "그건 전공은 정제 선배가 탑이거든."
    p "아, 정말? 괜찮은데?"
    pat "내가 대신 선배한테 연락해줄게. 학교 끝나고 제조 실습실 앞으로 가면 돼."
    p " 응, 알겠어! 고마워!"
 
#장면 전환 <제조 실습실>
    scene bg_dess with fade
    p "여기 맞지...?"
    ac "「조심스럽게 실습실 내부로 들어가자 정제 선배가 앞에 서 있었다.」"
    p "선배...! 실습 가르쳐준다 해주셔서 정말 감사합니다! 열심히 배우도록 하겠습니다!"
    show c_cho_n at c_center
    cho "... 그러던가."
    ac "「역시 여전히 과묵하고 무뚝뚝하다.」"
    p "(그래도 가르쳐준다 하는 게 어디야... 정말 다행이다.)"
    cho "두 번은 설명 안 해줄 거니까 잘 봐."
    p "네!"
    hide c_cho_n
    ac "「정말 두 번은 설명해주지 않을 것 같아서, 최대한 집중하며 설명을 들었다.」"
    cho "여기, 속에 들어갈 초콜릿을 템퍼링 하는 과정인데..."
    ac "「초콜릿을 젓는 손짓이 부드럽다. 한 두번 해본 솜씨가 아니야... 뭔가 좀... 멋있지 않나?」"
    ac "「가만히 서서 선배의 손목 움직임을 보니 잠이 몰려오는 것 같기도 했다.」"
    ac "「자면 안 되는데, 자꾸만 고개가 기울어진다.」"

    show c_cho_n at c_center
    cho "... 전학생."
    p "느에?!" with vpunch
    ac "「깜짝 놀라 대답을 하자, 입 안에 달콤한 맛이 나는 손가락이 들어왔다.」"
    p "(잠깐, 손가락?)"
    cho "피곤할 때는, 당분을 보충하는 게 좋아."
    hide c_cho_n


    menu cho_selection1 :
        "서, 선배?! ... 오, 맛있어...!" : #초코 1
            show c_cho_n at c_center
            ac "「선배의 어깨가 살짝 올라간 것처럼 보인다.」"
            cho "어제 실습하고 남은 초콜릿이야. 하루 지나도 맛있어."
            p "와, 진짜 맛있어요."
            p "선배 천재라는 소문이 자자하더니 정말이었군요!!"
            cho "... 그정도는 아니야." #호감도 상승 이미지
            jump cho_study2
       
        "선배... 손은 닦으신 거죠...?" : #게임 오버
            show c_cho_m at c_center
            cho "......" #경멸
            jump gameover
       
        "와, 대박!!! 진짜 맛있어요! 선배 이거 하나 더 있어요?" : #초코 2
            show c_cho_h at c_center
            cho "... 입맛에 맞아?" #호감도 상승 이미지
            p "이건 초코릿을 싫어하는 사람들도 맛있다고 할 거라구요!"
            p "선배는 천재예요, 천재!"
            p "잠도 완전히 달아났어요! 각성제가 따로 없네요!"
            cho "... 그렇다니 다행이네."
            jump cho_study2


label cho_study2 :
    show c_cho_n at c_center
    p "감사합니다. 이제 안 졸게요!"
    cho "더 졸지 마, 분명 한 번만 보여준다고 했어."
    p "그럼요! 잠도 깼으니 집중 잘 할게요!"
    cho "그럼... 이제 빵 반죽을 만들 건데, 물과 밀가루의 비율은 이 정도로 해야 빵의 겉이 바삭해져."
    p "오 그렇구나..."
    cho "그리고... 다음은 속 재료와 반죽이 완성되었으니 붕어빵을 만들어 봐야겠지."
    cho "여기 있는 붕어빵 틀을 이용해서 구워줄 거야. 불 조절 하는 거 잘 봐."
    p "(......?)"
    p "(저거 무쇠 팬이야? 엄청 무거울 텐데, 저걸 한 손으로...)"
    p "선배 말 잘 들을게요."
    cho "... 갑자기?"
    p "그냥요... 선배가 너무 강력해 보여서..."
    cho "... 뭐, 그러던가..."
    cho "이상한 소리 그만하고 이제 네가 한 번 만들어봐. \n봐줄게."
    hide c_cho_h    
    hide c_cho_n

    p "(아까 선배가 보여준 대로! 할 수 있다!)"
    p "(선배도 힘들 테니 최대한 빨리 끝내겠다는 의지를 불태우며, 화력을 최대로 올렸다.)"

    cho "......?"
    cho "잠깐,"

    p "(달궈지기까지 기다려야 하나?)"
    ac "「잘 몰라서 일단 오일을 틀에 발랐다.」"
    ac "「팬에 발려진 오일이 금세 보글거리기 시작하자, 반죽을 부었다.」"
    ac "「반죽이 기름에 닿자마자, 뭔가 팬에서 터지는 소리가 났고, \n동시에 팬 위에 거대한 뚜껑이 덮어졌다.」"

    show c_cho_n at c_center
    cho "... 이 바보가..."
    cho "온도를 그렇게 올리면 어쩌자는 거야?"
    cho "기름이 너무 달궈졌을 때 반죽을 넣으면 갑자기 터질 때가 있단 말이야!"
    hide c_cho_n


    menu cho_selection2 :
        "아니, 그런 건 빨리 알려줬어야죠!" : #게임 오버
            show c_cho_m at c_center
            cho "너 지금 그것도 모르면서 이 학교에 들어온 거야?" #경멸
            jump gameover


        "헉...! 그, 그건 몰랐어요! 죄송합니다!" : #초 1개?
            show c_cho_n at c_center
            cho "몰랐으면 물어보고 해야할 거 아냐."
            jump cho_study3
       
        "선배 괜찮으세요?! 죄송해요, 제가 조심했어야 하는데!!" : #초 2개
            $ item_boong = 2
            $ item_cho_1 = 1
            show cho_1 at cho_1_center
            "초콜릿 한 개를 얻었다!\n3개를 모으면 초콜릿 붕어빵을 만들 수 있다"
            hide cho_1
            show c_cho_h at c_center
            cho "나는 신경 쓰지 말고, 다음부턴 조심해."
            cho "너 위험할 뻔 했어."
            
            jump cho_study3


label cho_study3 :
    scene bg_dess
    p "죄송해요, 저 가르쳐 주시느라 힘드실까 봐 빨리 끝내려다 그랬어요..."
    show c_cho_n at c_center
    ac "「선배가 내 앞에서 한숨을 쉬며 불을 끄고, 잠시 기다렸다가 뚜껑을 치웠다.」"
    cho "내가 알려준다고 남은 건데, 왜 신경을 쓰는 거야?"
    cho "됐고, 이리 와봐."


    ac "「선배가 달궈진 팬을 치우고 새로운 팬을 꺼냈다.」"
    ac "「내 뒤에 서서, 내 손을 잡으며 천천히 하나씩 알려주었다.」"
    ac "「선배한테서 나는 미묘한 초콜릿 냄새와, 내 손을 잡은 부드러운 손 길에 심장이 빨리 뛰는 느낌이 든다.」"
    p "(아, 이러면 안 되는데...! 집중해야 한다고...!)"


    cho "... 너, 얼굴이 빨간데."
    p "지, 진짜요? 하하... 불 앞이라 그런가? 조금 더운 것 같기도 하고~"
    ac "「갑자기 선배가 나를 지긋이 쳐다보았다.」"
    cho "오늘은 그만. 지금 집중도 못 하고, 이러다 또 사고 낼 거 같아."
    p "엑...? 오늘 그만두면 마지막이고 그런 건 아니죠?"
    p "다음 수업도 있는 거죠?"
    show c_cho_h at c_center
    cho "시끄러워. '오늘은'이라고 했잖아. 이해 못 하는 건 아니지?"
    p "헉, 넵!! 저 오늘 배운 거 열심히 복습해 올게요, 선배!!"
    cho "그러든지. 먼저 들어가, 내가 치우고 갈 테니까."
    cho "전학생은 아직 정리하는 법 모르잖아?"
    p "아하하... 그럼 사양 않고 먼저 가보겠습니다!"
    ac "「그렇게 나는 다음 수업을 기대하며 학교를 나와 집으로 향했다.」"
    hide c_cho_n
    hide c_cho_h
    if chooseTang == 1 :
        $ item_boong = 2
        $ item_pat_1 = 2
        $ item_shu_1 = 2
        $ item_cho_1 = 2
        $ item_pi_1 = 2
        $ item_tang_5 = 1
        jump testTangAppear


    elif chooseTang == 0 :
        jump test




label testTangAppear :
    stop music fadeout 1.0
    play music end_song volume 1.0
    scene bg_class_1 with fade
    
    ac "「그렇게 오지 않았음 좋겠던 시험 당일이 왔다.」"
    p "(열심히 했으니까 잘할 수 있겠지...?)"
    boong "자~ 오늘은 시험 보는 날이죠? 다들 열심히 준비 했으리라 믿고~"
    boong "아, 맞아. [pname]이 옆에 자리가 하나 더 생겼을 거야."
    boong "거긴 오늘 현이가 시험 보러 오기로 해서 선생님이 마련해둔 자리니까, \n그렇게 알고 있으려무나~"
    p "(응? 현이가 누구지? 내 친구 중에도 현이라는 애가 있었는데... \n걔랑 이름이 똑같네, 신기하다.)"
    p "(어쨌든, 시험을 봐야 하니까 책상은 띄워놓자...)"
    ac "「책상을 띄워 두고, 자리에 앉아 요점정리한 노트를 펼쳤다.」"


    ac "「드르륵ㅡ」"


    ac "「교실 문이 열리는 소리가 나고, 발소리가 내 쪽으로 점차 가까워지는 게 느껴졌다. 」"
    p "(아, 그 현이라는 친구 왔나보네.)"
    ac "「신경 쓰지 않고 내 공부를 계속 하고 있는데, 그 애가 내 어깨를 톡톡 건드렸다.」"

    show c_tang_n at t_center
    $ item_boong = 2
    $ item_pat_1 = 2
    $ item_shu_1 = 2
    $ item_cho_1 = 2
    $ item_pi_1 = 2
    $ item_tang_1 = 1
    tang "... 저기, 혹시 너 [pname]이?"
    p "응? ... 어, 너는!!!"
    tang "나 기억하는 눈치네. 오랜만이야, [pname]아."
    p "넌 아직 이 동네에서 지내고 있나 보구나... 이렇게 만나게 돼서 너무 다행이다."
    p "그렇게 헤어진 뒤로 못볼 줄 알았는데......"
    tang "응, 그러게..."


    ac "「딩동댕동ㅡ」"
    tang "아, 종이 눈치가 없네. 할 말이 많은데."
    tang "아쉽지만, 시험 끝나고 얘기 하자."
    hide c_tang_n
    show c_tang_h at t_center
    tang "시험, 잘 봐."
    hide screen inventory_display_toggle
    jump ending


label test :
    scene bg_class_1 with fade
    ac "「그렇게 오지 않았음 좋겠던 시험 당일이 왔다.」"
    p "(열심히 했으니까 잘할 수 있겠지...?)"
    boong "자~ 오늘은 시험 보는 날이죠? 다들 열심히 준비 했으리라 믿고~"
    boong "시험 시작 할게요~"
    hide screen inventory_display_toggle
    jump ending


   
label gameover:
    call screen game_over
    return 
    
label ending :
    call screen goodbye



