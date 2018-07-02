import media 
import fresh_tomatoes

cindrella = media.Movie('cindrella',
                        'a poor girl who making the prnce fallinng in love with her',
                        'file:///C:/Users/Bonjour/Desktop/assepoester-1.20170303020003.jpg',
                        'https://www.youtube.com/watch?v=20DF6U1HcGQ')


black_panthar = media.Movie('black panthar',
                            'a cool movie is it a sequence of marva',
                            'file:///E:/MY%20LIFE/girl.jpg',
                            'https://www.youtube.com/watch?v=xjDjIWPwcPU')
game_night = media.Movie('game night',
                         ' a couple who gone through a lot of facts in thier game night ',
                         'file:///E:/MY%20LIFE/pexels-photo.jpg',
                         'https://www.youtube.com/watch?v=qmxMAdV6s4U')
the_little_mermaid = media.Movie('the little mermaid',
                                 'a triditional story of the mermaid',
                                 'file:///E:/MY%20LIFE/pexels-photo-54203.jpg',
                                 'https://www.youtube.com/watch?v=e4LfNLtVQqE')
# print game_night.show_trailer()
movies = [cindrella,black_panthar, game_night,the_little_mermaid ]
fresh_tomatoes.open_movies_page(movies)


