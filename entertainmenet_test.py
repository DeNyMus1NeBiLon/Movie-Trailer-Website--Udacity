# Importing the fresh_tomatoes module which helps
# to generate & render the html page using python code
import fresh_tomatoes

# Importing the mypage module where the
# constructer is initialized for movies as parameters
import mypage

# Creates 15 different movie trailer instance of Theatre class with
# 4 parameters(movie_title, movie_storyline, poster_image, trailer_youtube)
toy_story = mypage.Movie(
    "Toy Story",
    "A boy who have toys",
    "https://vignette.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",  # noqa
    "https://www.youtube.com/watch?v=xmzbwheRutk")

avatar = mypage.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = mypage.Movie(
    "School of Rock",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/fi/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

rotatouille = mypage.Movie(
    "Rotatouille",
    "A Rat is a chef in Paris",
    "https://upload.wikimedia.org/wikipedia/de/f/fd/Ratatouille-Film.JPG",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = mypage.Movie(
    "Midnight in Paris",
    "Going back in time to meet Authors",
    "https://vignette.wikia.nocookie.net/midnightinparis/images/a/a9/Midnight-in-paris-header.jpg/revision/latest?cb=20130424031150",  # noqa
    "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = mypage.Movie(
    "Hunger Games",
    "A really reality real show ",
    "https://vignette.wikia.nocookie.net/dietributevonpanem/images/a/a5/250px-O-FINAL-HUNGER-GAMES-POSTER-570.jpg/revision/latest?cb=20120401064801&path-prefix=de",  # noqa
    "https://www.youtube.com/watch?v=4S9a5V9ODuY")

gangs_of_ny = mypage.Movie(
    "Gangs of New York",
    "Amsterdam returns to Five Points ,"
    "to get revenge on his father's killer",
    "https://upload.wikimedia.org/wikipedia/en/a/ae/Gangs_of_New_York_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=qHVUPri5tjA")

pulp_fiction = mypage.Movie(
    "Pulp Fiction",
    "Storylines of mobsters,  "
    "fringe players, small-time criminals, "
    "and a mysterious briefcase",
    "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=tGpTpVyI_OQ")

divergent = mypage.Movie(
    "Divergent",
    "A thrilling action-adventure film set  "
    "in a world where people are  "
    "divided into distinct factions based on human virtues.",
    "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
    "https://youtu.be/336qJITnDi0")

insurgent = mypage.Movie(
    "The Divergent Series: Insurgent",
    "Insurgent raises the stakes for "
    " Tris as she searches for allies and "
    " answers in the ruins of a futuristic Chicago.",
    "https://upload.wikimedia.org/wikipedia/en/a/af/Insurgent_poster.jpg",
    "https://youtu.be/sX9-l0iO5w4")

allegiant = mypage.Movie(
    "The Divergent Series: Allegiant",
    "After the earth-shattering revelations of INSURGENT,  "
    "  Tris must escape with Four and go beyond the wall enclosing Chicago.",
    "https://upload.wikimedia.org/wikipedia/en/f/f8/Allegiantfilmposter.jpg",
    "https://www.youtube.com/watch?v=0G0C-vMHcQY")

ascendant = mypage.Movie(
    "The Divergent Series: Ascendant",
    "After Allegiant is Ascendant which is to arrive in 2017",
    "http://www.thedivergentseries.movie/ascendant/assets/img/poster/poster.jpg",  # noqa
    "https://youtu.be/6DWqWGwIATQ")

star_trek = mypage.Movie(
    "Star Trek",
    "The greatest adventure of all time begins with Star Trek,  "
    "the incredible story of a young crew's maiden voyage onboard "
    " the most advanced starship ever created: the U.S.S. Enterprise.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
    "https://youtu.be/iGAHnZ555nI")

star_trek_into_darkness = mypage.Movie(
    "Star Trek Into Darkness",
    "When a ruthless mastermind,  "
    "Khan (Benedict Cumberbatch,) declares a one-man war "
    "on the Federation, Captain Kirk (Chris Pine),  "
    "Spock (Zachary Quinto), and the crew of the U.S.S. Enterprise "
    "set out on their most explosive manhunt of all time.",
    "https://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",  # noqa
    "https://youtu.be/sJNyGFqgyag")

interstellar = mypage.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an",
    "https://vignette.wikia.nocookie.net/interstellarfilm/images/6/6f/Interstellar_website.jpg/revision/latest?cb=20140923050808",  # noqa
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

#  Code Array, Array python LIST
movies = [
    toy_story,
    avatar,
    school_of_rock,
    rotatouille,
    midnight_in_paris,
    hunger_games,
    gangs_of_ny,
    pulp_fiction,
    divergent,
    insurgent,
    allegiant,
    ascendant,
    star_trek,
    star_trek_into_darkness,
    interstellar]
#  Display the movie page!
fresh_tomatoes.open_movies_page(movies)
