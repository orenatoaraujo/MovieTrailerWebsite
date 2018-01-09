import fresh_tomatoes
import media

star_wars_episode_4 = media.Movie("Star Wars: Episode IV - A New Hope", "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg", "https://www.youtube.com/watch?v=vZ734NWnAHA")
star_wars_episode_5 = media.Movie("Star Wars: Episode V - The Empire Strikes Back", "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg", "https://www.youtube.com/watch?v=JNwNXF9Y6kY")
star_wars_episode_6 = media.Movie("Star Wars: Episode VI - Return of the Jedi", "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg", "https://www.youtube.com/watch?v=7L8p7_SLzvU")
star_wars_episode_1 = media.Movie("Star Wars: Episode I - The Phantom Menace", "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg", "https://www.youtube.com/watch?v=bD7bpG-zDJQ")
star_wars_episode_2 = media.Movie("Star Wars: Episode II - Attack of the Clones", "https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg", "https://www.youtube.com/watch?v=gYbW1F_c9eM")
star_wars_episode_3 = media.Movie("Star Wars: Episode III - Revenge of the Sith", "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg", "https://www.youtube.com/watch?v=5UnjrG_N8hU")

movies = [star_wars_episode_4, star_wars_episode_5, star_wars_episode_6, star_wars_episode_1, star_wars_episode_2, star_wars_episode_3]

fresh_tomatoes.open_movies_page(movies)
