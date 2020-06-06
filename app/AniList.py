import xml.etree.ElementTree as ET

class AniList:
    def __init__(self, username):
        self.username = username
        self.filename = 'app/animelists/animelist_{}.xml'.format("".join(username))
        self.tree = ET.parse(self.filename)
        self.root = self.tree.getroot()

    def __str__(self):
        return ET.tostring(self.root, encoding='utf8').decode('utf8')

    def addAnime(self, series_title, series_type, series_episodes, my_watched_episodes, my_score, my_status, my_times_watched):
        anime = ET.SubElement(self.root, 'anime')
        anime.text = '\n\t\t\t\t\t'
        series_animedb_id = ET.SubElement(anime, 'series_animedb_id')
        series_animedb_id.tail = '\n\t\t\t\t\t'
        title = ET.SubElement(anime, 'series_title')
        title.text = series_title
        title.tail = '\n\t\t\t\t\t'
        stype = ET.SubElement(anime, 'series_type')
        stype.text = series_type
        stype.tail = '\n\t\t\t\t\t'
        s_ep = ET.SubElement(anime, 'series_episodes')
        s_ep.text = series_episodes
        s_ep.tail = '\n\t\t\t\t\t'
        my_id = ET.SubElement(anime, 'my_id')
        my_id.tail = '\n\t\t\t\t\t'
        w_ep = ET.SubElement(anime, 'my_watched_episodes')
        w_ep.text = my_watched_episodes
        w_ep.tail = '\n\t\t\t\t\t'
        my_start_date = ET.SubElement(anime, 'my_start_date')
        my_start_date.tail = '\n\t\t\t\t\t'
        my_finish_date = ET.SubElement(anime, 'my_finish_date')
        my_finish_date.tail = '\n\t\t\t\t\t'
        my_rated = ET.SubElement(anime, 'my_rated')
        my_rated.tail = '\n\t\t\t\t\t'
        score = ET.SubElement(anime, 'my_score')
        score.text = my_score
        score.tail = '\n\t\t\t\t\t'
        my_dvd = ET.SubElement(anime, 'my_dvd')
        my_dvd.tail = '\n\t\t\t\t\t'
        my_storage = ET.SubElement(anime, 'my_storage')
        my_storage.tail = '\n\t\t\t\t\t'
        status = ET.SubElement(anime, 'my_status')
        status.text = my_status
        status.tail = '\n\t\t\t\t\t'
        my_comments = ET.SubElement(anime, 'my_comments')
        my_comments.tail = '\n\t\t\t\t\t'
        times_watched = ET.SubElement(anime, 'my_times_watched')
        times_watched.text = my_times_watched
        times_watched.tail = '\n\t\t\t\t\t'
        my_rewatch_value = ET.SubElement(anime, 'my_rewatch_value')
        my_rewatch_value.tail = '\n\t\t\t\t\t'
        my_tags = ET.SubElement(anime, 'my_tags')
        my_tags.tail = '\n\t\t\t\t\t'
        my_rewatching = ET.SubElement(anime, 'my_rewatching')
        my_rewatching.tail = '\n\t\t\t\t\t'
        my_rewatching_ep = ET.SubElement(anime, 'my_rewatching_ep')
        my_rewatching_ep.tail = '\n\t\t\t\t\t'
        update_on_import = ET.SubElement(anime, 'update_on_import')
        update_on_import.tail = '\n\t\t\t\t'
        anime.tail = '\n\t\t\t\n\t\t\t\t'

        self.tree.write(self.filename)


    def delAnime(self, series_title):
        for anime in self.root.findall('./anime'):
            if anime[1].text == series_title:
                self.root.remove(anime)
        self.tree.write(self.filename)

    def getAnimeList(self):
        return self.root.findall("./anime")

    def getAnime(self, series_title):
        return self.root.find("./anime/[series_title='{}']".format(''.join(series_title)))

    def getAnimeParam(self, series_title, parameter):
        anime = self.getAnime(series_title)
        for param in anime:
            if param.tag == parameter:
                return param

    def modAnime(self, series_title, parameter, new_value):
        anime = self.getAnime(series_title)
        for param in anime:
            if param.tag == parameter:
                param.text = new_value
        self.tree.write(self.filename)