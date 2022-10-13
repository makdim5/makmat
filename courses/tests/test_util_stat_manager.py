import pytest
from django.contrib.auth.models import User

from courses.utils import *


# StatisticsManager testing

# get_stat_for_topic testing
@pytest.mark.django_db
def test_get_stat_for_topic_with_tasks_user_with_results():
    topic, user = Topics.objects.filter(id=3)[0], User.objects.filter(id=2)[0]
    assert list(Tasks.objects.filter(topic=topic)) != []
    expected = 100
    assert StatisticsManager.get_statistics_for_topic(topic, user) == expected


@pytest.mark.django_db
def test_get_stat_for_empty_topic_and_user():
    topic, user = Topics(), User()
    assert list(Tasks.objects.filter(topic=topic)) == []
    expected = 0
    assert StatisticsManager.get_statistics_for_topic(topic, user) == expected


@pytest.mark.django_db
def test_get_stat_for_topic_with_tasks_user_no_results():
    topic, user = Topics.objects.filter(id=3)[0], User.objects.filter(id=12)[0]
    assert list(Tasks.objects.filter(topic=topic)) != []
    expected = 0
    assert StatisticsManager.get_statistics_for_topic(topic, user) == expected


@pytest.mark.django_db
def test_get_stat_for_no_topic_and_no_user():
    topic, user = {}, "nkjn"
    expected = 0
    assert StatisticsManager.get_statistics_for_topic(topic, user) == expected


@pytest.mark.django_db
def test_get_stat_for_topic_with_no_tasks():
    topic, user = Topics.objects.filter(id=2)[0], User.objects.filter(id=12)[0]
    assert list(Tasks.objects.filter(topic=topic)) == []
    expected = 0
    assert StatisticsManager.get_statistics_for_topic(topic, user) == expected


# get_stat_for_section testing
@pytest.mark.django_db
def test_get_stat_for_section_with_no_topics():
    section, user = Sections(), User.objects.filter(id=12)[0]
    assert list(Topics.objects.filter(section=section)) == []
    expected = 0
    assert StatisticsManager.get_statistics_for_section(section, user) \
           == expected


@pytest.mark.django_db
def test_get_stat_for_section_with_topics():
    section, user = Sections.objects.filter(id=1)[0], User.objects.filter(id=2)[0]
    assert list(Topics.objects.filter(section=section)) != []
    expected = 50
    assert StatisticsManager.get_statistics_for_section(section, user) \
           == expected


@pytest.mark.django_db
def test_get_stat_for_section_with_incorrect_data():
    section, user = [0], "some_text"
    expected = 0
    assert StatisticsManager.get_statistics_for_section(section, user) \
           == expected
