"""
Check the correctness of the get lyrics function with Genius API.
"""

# Import all required libraries.
import pytest

# Import the functions
from genius_get_lyrics import (
    first_number_index,
    getlyrics,
    get_lyrics_dictionary,
)


@pytest.mark.parametrize(
    "source_text,index",
    [
        # Check that a simple string with a number in the middle
        ("aaaaaaa7aa", 7),
        # Checks if there are no numbers
        ("aaaa", -1),
        # Checks the first index
        ("7aaa", 0),
        # Checks the last index
        ("aaa7", 3),
        # Checks if there are more than one number, it returns the first
        ("aaa7aa7", 3),
    ],
)
def test_first_number_index(source_text, index):
    """
    Check that the index of the first number from the input text
    is correct.

    Args:
        source_text: A string representing the source text.
        index: An int representing the index of the first number.

    """
    assert first_number_index(source_text) == index


@pytest.mark.parametrize(
    "artist,song,lyrics",
    [
        # Check a random song
        (
            "Gracie Abrams",
            "21",
            (
                "I missed your 21st birthday, I've been up at home Almost tried"
                " to call you, don't know if I should Hate to picture you"
                " half-drunk happy Hate to think you went out without me I'm"
                " sorry if you blame me, if I were you, I would Thought you'd"
                " see it comin', but you never could I still haven't heard from"
                " your family But you said your mom always loved me Sometimes I"
                " go blurry-eyed Small talk and you tell me that you're on fire"
                " Lights on and it's black and white, I couldn't stay forever I"
                " see the look in your eye and I'm bitin' my tongue You'll be"
                " the love of my life when I was young When the night is over"
                " Don't call me up, I'm already under I get a little bit alone"
                " sometimes and I miss you again I'll be the love of your life"
                " inside your head When the night is over Don't call me up, I'm"
                " already under Audrey said she saw you out past twelve o'clock"
                " Just because you're hurtin' doesn't mean I'm not If it"
                " doesn't go away by the time I turn thirty I made a mistake"
                " and I'll tell you I'm sorry \"Sorry\" You might also like"
                " Sometimes I go blurry-eyed Small talk and you tell me that"
                " you're on fire Lights on and it's black and white, I couldn't"
                " stay forever I see the look in your eye and I'm bitin' my"
                " tongue You'll be the love of my life when I was young When"
                " the night is over Don't call me up, I'm already under I get a"
                " little bit alone sometimes and I miss you again I'll be the"
                " love of your life inside your head When the night is over"
                " Don't call me up, I'm already under"
            ),
        ),
        # Check song that isn't in english
        (
            "Jung Kook",
            "Still With You",
            (
                "날 스치는 그대의 옅은 그 목소리 내 이름을 한 번만 더"
                " 불러주세요 얼어버린 노을 아래 멈춰 서있지만 그대 향해 한"
                " 걸음씩 걸어갈래요 Still with you 어두운 방 조명 하나 없이"
                " 익숙해지면 안 되는데 그게 또 익숙해 나지막이 들리는 이 에어컨"
                " 소리 이거라도 없으면 나 정말 무너질 것 같아 함께 웃고 함께"
                " 울고 이 단순한 감정들이 내겐 전부였나 봐 언제쯤일까 다시 그댈"
                " 마주한다면? 눈을 보고 말할래요 보고 싶었어요 You might also"
                " like 황홀했던 기억 속에 나 홀로 춤을 춰도 비가 내리잖아 이"
                " 안개가 걷힐 때쯤 젖은 발로 달려갈게 그때 날 안아줘 저 달이"
                " 외로워 보여서 밤하늘에 환하게 울고 있는 것 같아서 언젠가"
                " 아침이 오는 걸 알면서도 별처럼 너의 하늘에 머물고 싶었어"
                " 하루를 그 순간을 이렇게 될 걸 알았다면 더 담아뒀을 텐데"
                " 언제쯤일까 다시 그댈 마주한다면 눈을 보고 말할래요 보고"
                " 싶었어요 황홀했던 기억 속에 나 홀로 춤을 춰도 비가 내리잖아"
                " 이 안개가 걷힐 때쯤 젖은 발로 달려갈게 그때 날 잡아줘 날"
                " 바라보는 희미한 미소 뒤편에 아름다운 보랏빛을 그려볼래요 서로"
                " 발걸음이 안 맞을 수도 있지만 그대와 함께 이 길을 걷고 싶어요"
                " Still with you"
            ),
        ),
    ],
)
def test_getlyrics(artist, song, lyrics):
    """
    Check the lyrics matches the actual lyrics from artist
    and song after getting rid of all the extra words.

    Args:
        artist: A string representing the artist title.
        song: A string representing the song title.
        lyrics: A string representing the lyrics.

    """
    assert getlyrics(artist, song) == lyrics


@pytest.mark.parametrize(
    "usernames,top_tracks,dictionary",
    [
        # Check list of one username of top 2 tracks
        (
            ["sgekrmt9z1gdutogll2zmg9ny"],
            [
                (
                    ("Wasia Project", "Petals on the Moon"),
                    ("Julie Andrews", "The Lonely Goatherd"),
                )
            ],
            {
                "sgekrmt9z1gdutogll2zmg9ny": [
                    (
                        "Feeling down Orange juice Cigarette To get me through"
                        " As it rains I conclude I need help From someone new"
                        " So take me in your spaceship Throw me up into new"
                        " places Blast me into silence Let your guidance get me"
                        " through this Gravity is pulling me Along and I can't"
                        " find a way To understand Why I'm here again and"
                        " again, oh I feel like everybody's singing out of tune"
                        " I feel like I can't help but always be so blue But in"
                        " the end I know I must keep pulling through And brace"
                        " myself for all the hell-likе petals on the moon You"
                        " might also like Feeling cold Train delayеd You've"
                        " gone home And I'm afraid Helios Sun divine Hold me up"
                        " Into the sky You take me in your spaceship Throw me"
                        " up to constellations Blast me into silence Let your"
                        " guidance get me through this Gravity is pulling me"
                        " Along and I can't find a way To understand Why I'm"
                        " here again and again, oh I feel like everybody's"
                        " singing out of tune (I feel so blue) I feel like I"
                        " can't help but always be so blue (Keep pulling"
                        " through) But in the end I know I must keep pulling"
                        " through And brace myself for all the hell-like petals"
                        " on the moon Born again, alone again, again Home"
                        " again, you're gone again, again, again Will somebody"
                        " be there for me when all my friends have left? Even"
                        " if I'm undone in the end, ooh I feel like everybody's"
                        " singing out of tune (I feel so blue) I feel like I"
                        " can't help but always be so blue (Keep pulling"
                        " through) But in the end I know I must keep pulling"
                        " through And brace myself for all the hell-like petals"
                        " on the moon Embe"
                    ),
                    None,
                ]
            },
        ),
        # Check list of multiple usernames of top 2 tracks
        (
            ["cmot17", "sgekrmt9z1gdutogll2zmg9ny"],
            [
                (("I DONT KNOW HOW BUT THEY FOUND ME", "Do It All The Time"),),
                (("Wasia Project", "Petals on the Moon"),),
            ],
            {
                "cmot17": [
                    "Ha! We're taking over the world One kiss at a time And"
                    " then I'm taking your girl And I'm making her mine No"
                    " reason why I'm only doing anything I want to do Because I"
                    " do it all the time We're taking over the world A little"
                    " victimless crime And when I'm taking your innocence I'll"
                    " be corrupting your mind No need to cry I'm only doing"
                    " anything I want to do Because I do it all the time (Do it"
                    " all the time) You might also like Now we're so young, but"
                    " we're probably gonna die It's so fun, we're so good at"
                    " selling lies We look so good and we never even try Get"
                    " your money from a trust fund Do it all the time Ha! We're"
                    " taking over the world One kiss at a time And then I'm"
                    " taking your girl And I'm making her mine, I'm making her"
                    " mine No reason why I'm only doing anything I want to do"
                    " (Do it all the time) Now we're so young, but we're"
                    " probably gonna die And it's so fun, we're so good at"
                    " selling lies We look so good and we never even try I"
                    " don't wanna do it, but I'll do it 'cause I do it all the"
                    " time Now we're so young, but we're probably gonna die"
                    " It's so fun, we're so good at selling lies We look so"
                    " good and we never even try Get your money from a trust"
                    " fund Do it all the time"
                ],
                "sgekrmt9z1gdutogll2zmg9ny": [
                    "Feeling down Orange juice Cigarette To get me through As"
                    " it rains I conclude I need help From someone new So take"
                    " me in your spaceship Throw me up into new places Blast me"
                    " into silence Let your guidance get me through this"
                    " Gravity is pulling me Along and I can't find a way To"
                    " understand Why I'm here again and again, oh I feel like"
                    " everybody's singing out of tune I feel like I can't help"
                    " but always be so blue But in the end I know I must keep"
                    " pulling through And brace myself for all the hell-likе"
                    " petals on the moon You might also like Feeling cold Train"
                    " delayеd You've gone home And I'm afraid Helios Sun divine"
                    " Hold me up Into the sky You take me in your spaceship"
                    " Throw me up to constellations Blast me into silence Let"
                    " your guidance get me through this Gravity is pulling me"
                    " Along and I can't find a way To understand Why I'm here"
                    " again and again, oh I feel like everybody's singing out"
                    " of tune (I feel so blue) I feel like I can't help but"
                    " always be so blue (Keep pulling through) But in the end I"
                    " know I must keep pulling through And brace myself for all"
                    " the hell-like petals on the moon Born again, alone again,"
                    " again Home again, you're gone again, again, again Will"
                    " somebody be there for me when all my friends have left?"
                    " Even if I'm undone in the end, ooh I feel like"
                    " everybody's singing out of tune (I feel so blue) I feel"
                    " like I can't help but always be so blue (Keep pulling"
                    " through) But in the end I know I must keep pulling"
                    " through And brace myself for all the hell-like petals on"
                    " the moon Embe"
                ],
            },
        ),
    ],
)
def test_get_lyrics_dictionary(usernames, top_tracks, dictionary):
    """
    Check that the index of the first number from the input text
    is correct.

    Args:
        usernames: A list of spotify usernames.
        top_tracks: A list of songs representing top tracks.
        dictionary: A dictionary mapping list of lyrics to username.

    """
    assert get_lyrics_dictionary(usernames, top_tracks) == dictionary
