# cs1-pong
Two-player game inspired by 1972 Atari Pong with some other special power-ups / settings.

## More Details
We implemented this game in my introductory CS class and it was so rewarding!! I really loved this game (as you can see from the fanatically scribbled ideas below) and I've included two versions of code from this project. The first is the game with the baseline requirements given to us in class and the second ('EC' version) has some of the cool power-ups and ideas I thought of. An overview of the special effects I added:
    - current score
    - high score
    - color scheme change @ 11th hit
    - random velocities
    - standardized speed
    - paddle positions centered
    - ball accelerated when paddle is in motion during collision
    - animation for hitting the center of the paddle
    - .......

My next steps as I wrote them for myself (this document is essentially a formalized version of my notes doc from when I created this code):
    (1.) animation for hitting the center of the paddle? [IN PROGRESS]
          --> maybe i should center the confetti around the ball instead of the paddle so it doesn't decapitate
    (2.) or for hitting the ball while the paddle is still?
    (3.) how do we combat the y acceleration, because x does not have the opportunity to accelerate! :)?
        i'm thinking that it should be hitting while still so that it's a mroe direct opposite.
    (4.) so then only points for hitting the center of the paddle i guess?
    (5.) oh maybe points for hitting center or hitting just the edge!!?!?
    (6.) should the game speed up as time progresses
    (7.) hehe dinosaur game, change black and white opposites

    scores for center vs. edges. center is harder to do, so you get a hardball for every 3 in a row.
    nested for loops for rows of balls to show how many powerups have been acquired?? maybe 3!! to do transparency

    this might be where collaborative and competitive mode start to split?
    a "good save!" deal? where you... hm how to measure this kind of thing?

## Other Cool Ideas I Wanted to Implement!!
    hehe my ideas for extra credit which I cannot do rn
    scoreboard
    wide screen vs. up close and personal
    collaborative vs. competitive
    power up, slo-mo when u need it, earn 1 every 15 hits you make?
                or fast ball, 1 every 30 hits you make? --> does this mean the paddles also go 2x
                NO ONLY KEEP POWER FOR CERTAIN AMT OF TIME, paddle color changes when you have a power (blue, red)
                    or maybe cumulative powers are not so bad, just get darker shade as you accumulate?
                or double ball, but one of them is fake, and you have to guess which one is real
    after 60 hits, little stick figure runs up and down the center line of the court and blocks your hits
        ohhhhhhhh have the score be the moving running man instead of actual running man
        HAHHA and then hitting it makes it go down lmao.. oh or up, depending on the mode?? oh wait we can't aim
        so then being able to respond makes it go back to original ohhhh
    omg UGH the power to mess with the other persons paddle would be SO FUNNY HAHHAHAH

    would it be cooler to have the paddles and ball and text all stay the same size but the window can change???????
        it would definitely be easier lmao, bc then size things can be permanent
        and maybe the user can customize their size at beginning??

    Random initial direction for the ball. (But make sure that it has enough horizontal and enough vertical
        component to be interesting. If the ball just goes up and down, or almost just up and down,
        the game is not going to be interesting.)
    having things speed up at 22?
    When the ball bounces off a moving paddle, accelerate the ball slightly in the direction of the paddle's motion
    Unpredictable bouncing
    Fancy .png images for ball and paddles
        --> hehe volleyball white color scheme
        persons face lmao
        omg then we could add SPIN!!! :o
    More than two players.
    Obstacles. Obstacles that accelerate the ball.
    Breakout, Arkanoid, or a pinball machine.
    oh!!! omg an invisible or visible place in the middle of the court which causes the ball to go random direction
        kind of like game pigeon mini golf lmao
        and then do they get something to reveal it? like... taking on a certain challenge ahead of time?
            oh!!! a great challenge would be already having the paddle at the right place
            so you have to hit the ball off a still paddle at least like 4 times or smth
            and then you get the reward of uv light vision :)))
            heheh this is starting to sound spy focused ahahahhaha
            OH A PRETTY VISUAL like light popping off, or confetti or something.
                to show that you did it off a still paddle
            LOLLZZZ after you earn it, it's like jetpack joyride mario kart,,, you get to click a button to prize
        ACK alternative idea i just came up with--> invisible paddles but ball has little light around it, oh
        OH OH OH OH during the black and white switch time!!!!!!! :)))))
    hehe a popup disclaimer in the middle of the game with an rgb color 2-line border :)
        telling you the rules, and then it won't tell you again afterwards
    omg this would be crazy to animate but i just had this daydream of
        like a space time web, faint circles around the ball and when it moves the circle oblongs and
        or maybe just semi circles showing a push in the direction of the ball
        or maybe opposite the direction of the ball
        just thought that would be so so pretty

    AHAHHHAHHHAHAH like in dinosaur game. ball or paddles flicker out and go dark, you have to keep track of yourself
    omg maybe a mouse interactive component, you have to click somewhere in order to get something, while still
        keeping the ball afloat

    if i put on website, can show old and ec version, and then also video of playing comethru or video game noise bkgd

    color of paddle gets lighter as move higher on screen, darker as you move lower on screen

    dad suggested three colors--?> could color the paddle or not, but make another powerup come from hitting the
        the ball in the center for certain number of times, then get different powerup :)
    should i make the players different colors?

    making ball into just outline instead of solid coloring?


## Bugs Solved / In Progress
okay i have a bug here to solve :)) START HERE
    key pressed
    2 20 20 True
    -33 -33 33 True
    -21 0 0 False
    and then the ball is frozen in the middle of the screen not going anywhere
    and if i press space again nothing happens...?

    uhhh i guess it fixed itself??
    NOPE! here's another example!
    -12 -18 18 True
    -33 0 0 False
    key pressed
    key pressed
    key pressed

    okay so the pattern seems to be when bvy = 0. and not sure if bvx being negative plays a role.

    well now it seems like all it took was just adding the 0. but technically bvx wasn't = 0 when the issue was
    occurring, so idk what happened with that...


2022_0904 bug
    sometimes the ball bounces off of air instead of the paddle???????????????????????????????
    I think we fixed this -- paddle position update error

middle of paddle collision animation
    i think the confetti might not always be working :(. maybe i should print all collision by's to see.
        actually i think it's just a close call more often than i realize! :))


