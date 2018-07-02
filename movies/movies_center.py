import fresh_tomatoes
import media

the_kissing_booth = media.Movie("The kissing booth", 
	"a girl who fell in love with had to get boy ", 
	"https://images.firstpost.com/wp-content/uploads/2018/05/kissing-booth-825.jpg",
	"https://www.youtube.com/watch?v=7bfS6seiLhk")

the_honor_list = media.Movie("The honor list", 
	"a story of good friendship with its ups and downs ", 
	"http://1.bp.blogspot.com/-Yr0nDY5MlY4/ThXmtSwnSxI/AAAAAAAABVY/fvc391AHJeM/s1600/larry+crowne+monte+carlo.jpg",
	"https://www.youtube.com/watch?v=Rxm_bVVhbr8")

the_table = media.Movie("The table",
" story of people who tells thier life to each ther while they r totally strangers to each other ", 
	"https://www.hancinema.net/photos/fullsizephoto872848.jpg", 
	"https://www.youtube.com/watch?v=fGGregNiTrU")

candy_jar = media.Movie("Candy jar", 
	"a story of the most competitive students on high school",
	"https://nypdecider.files.wordpress.com/2018/04/candy-jar1.jpg?quality=90&strip=all&w=720&h=480&crop=1",
	"https://www.youtube.com/watch?v=1lXLGwe_DUU&t=70s")

what_a_girl_wants = media.Movie("What a girl wants",
	"a story of teenage girl who travelling to london to see her father for the first time",
	"https://www.pastposters.com/cw3/assets/product_full/R/what-a-girl-wants-cinema-quad-movie-poster-(2).jpg",
	"https://www.youtube.com/watch?v=ah1L40a4X98")
family_weekend = media.Movie("Family weekend ",
	"a family that having troubles and their daughter trying to help them out in her way .", 
	"http://cdn01.cdn.justjared.com/wp-content/uploads/2013/03/cheno-family/kristin-chenoweth-oleysa-rulin-family-weekend-premiere-19.jpg",
	"https://www.youtube.com/watch?v=dS-TpNKVrtw")
# print family_weekend.show_trailer()
movies = [the_kissing_booth, the_honor_list, the_table, candy_jar, what_a_girl_wants, family_weekend]

#fresh_tomatoes.open_movies_page(movies)
# (media.Movie.VALID_RATINGS)
#print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__




