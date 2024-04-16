from unittest import main, TestCase
from ex_1_and_2.project import Hero


class TestHero(TestCase):
    HERO = {
        'username': 'hero',
        'level': 1,
        'health': 100.0,
        'damage': 10.0
    }

    ENEMY = {
        'username': 'enemy',
        'level': 1,
        'health': 100.0,
        'damage': 10.0
    }

    STAT_INCREASES_AFTER_WIN = {
        'level': 1,
        'health': 5,
        'damage': 5
    }

    def setUp(self):
        self.hero = Hero(username=self.HERO['username'],
                         level=self.HERO['level'],
                         health=self.HERO['health'],
                         damage=self.HERO['damage'])

        self.enemy = Hero(username=self.ENEMY['username'],
                          level=self.ENEMY['level'],
                          health=self.ENEMY['health'],
                          damage=self.ENEMY['damage'])

    def test_init(self):
        self.assertEqual(TestHero.HERO['username'], self.hero.username)
        self.assertEqual(self.HERO['level'], self.hero.level)
        self.assertEqual(TestHero.HERO['health'], self.hero.health)
        self.assertEqual(TestHero.HERO['damage'], self.hero.damage)

    def test_battle_versus_yourself_gives_exception(self):
        expected_error_type = Exception
        expected_error_message = "You cannot fight yourself"

        with self.assertRaises(expected_error_type) as ex:
            self.hero.battle(self.hero)

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_battle_with_insufficient_health_gives_value_error(self):
        expected_error_type = ValueError
        expected_error_message = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(expected_error_type) as ex:
            self.hero.health = 0
            self.hero.battle(self.enemy)

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_battle_with_enemy_with_insufficient_health_gives_value_error(self):
        expected_error_type = ValueError
        expected_error_message = f"You cannot fight {TestHero.ENEMY['username']}. He needs to rest"

        with self.assertRaises(expected_error_type) as ex:
            self.enemy.health = 0
            self.hero.battle(self.enemy)

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_battle_resulting_draw_decreases_both_players_health(self):
        self.hero.health = TestHero.ENEMY['damage']
        self.enemy.health = TestHero.HERO['damage']

        expected_result = "Draw"
        expected_hero_health = 0
        expected_enemy_health = 0

        self.assertEqual(expected_result, self.hero.battle(self.enemy))
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_enemy_health, self.enemy.health)

    def test_battle_resulting_hero_win_increases_player_level_health_damage(self):
        self.enemy.health = TestHero.HERO['damage']

        expected_result = "You win"
        expected_hero_level = TestHero.HERO['level'] + TestHero.STAT_INCREASES_AFTER_WIN['level']
        expected_hero_health = (TestHero.HERO['health'] - TestHero.ENEMY['damage']
                                + TestHero.STAT_INCREASES_AFTER_WIN['health'])
        expected_hero_damage = TestHero.HERO['damage'] + TestHero.STAT_INCREASES_AFTER_WIN['damage']

        self.assertEqual(expected_result, self.hero.battle(self.enemy))
        self.assertEqual(expected_hero_level, self.hero.level)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_hero_damage, self.hero.damage)

    def test_battle_resulting_enemy_win_increases_enemy_level_health_damage(self):
        self.hero.health = TestHero.ENEMY['damage']

        expected_result = "You lose"
        expected_enemy_level = TestHero.ENEMY['level'] + TestHero.STAT_INCREASES_AFTER_WIN['level']
        expected_enemy_health = (TestHero.ENEMY['health'] - TestHero.HERO['damage']
                                 + TestHero.STAT_INCREASES_AFTER_WIN['health'])
        expected_enemy_damage = TestHero.ENEMY['damage'] + TestHero.STAT_INCREASES_AFTER_WIN['damage']

        self.assertEqual(expected_result, self.hero.battle(self.enemy))
        self.assertEqual(expected_enemy_level, self.enemy.level)
        self.assertEqual(expected_enemy_health, self.enemy.health)
        self.assertEqual(expected_enemy_damage, self.enemy.damage)

    def test__str__outputs_correct_string(self):
        expected_string = f"Hero {TestHero.HERO['username']}: {TestHero.HERO['level']} lvl\n" \
                          f"Health: {TestHero.HERO['health']}\n" \
                          f"Damage: {TestHero.HERO['damage']}\n"

        self.assertEqual(expected_string, str(self.hero))


if __name__ == "__main__":
    main()
