import news

matches = ["identify it", "Quota exceeded"]


def select(types_factory=None):

    # Dictionary to map provider names to factory classes
    factory_mapping = {
        "TVMOVIES": QuestionTvMovies(),
        "LANDSCAPES": QuestionLandscapes(),
        "NEWS": QuestionNews(),
        "SPORTS": QuestionSports(),
    }

    factory = factory_mapping.get(types_factory)

    return factory


class QuestionTvMovies:

    def question(self):
        return "The image is a screen capture of a movie or a tv series episode. Can you tell me the name of the movie or series and the main actors?. If you can't identify it, just answer: I can't identify it."

    def post_process(self, answer):
        return answer


class QuestionLandscapes:

    def question(self):
        return "The image is a place in Earth, Can you tell me the name of the place and a description? If you can't identify it, just answer: I can't identify it."

    def post_process(self, answer):
        return answer


class QuestionSports:

    def question(self):
        return "The image is a capture of a tv sports cast. Can you tell me details about the teams and the match?. No more than 40 words about this. If you can't identify it, just answer: I can't identify it."

    def post_process(self, answer):
        print("Recognize:" + answer)
        if any(x in answer for x in matches):
            newsabouttopic = answer
        else:
            newsabouttopic = (
                answer + "\n" + "News about this topic:" + news.getNews(answer, 2)
            )
        return newsabouttopic


class QuestionNews:

    def question(self):
        return "The image is a capture of a tv newscast. Can you tell me what sibject are you seeing? I need it in twelve words or less (and ignore information about the tv network).  If you can't identify it, just answer: I can't identify it."

    def post_process(self, answer):
        if any(x in answer for x in matches):
            newsabouttopic = answer
        else:
            newsabouttopic = "News about this topic:" + news.getNews(answer, 3)
        return newsabouttopic

