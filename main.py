# This is a sample Python script.
import git
from deepdiff import DeepDiff
import yaml


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def test_fun(name):
    repo = git.Repo()
    index = repo.index
    head_diff = index.diff(None)

    for diff_added in head_diff:
        print(diff_added)
        commit = repo.commit('master')
        file_path = diff_added.a_path
        if "YamlConfig" in file_path:
            previous_config_yaml = yaml.safe_load(repo.git.show('{}:{}'.format(commit.hexsha, file_path)))
            current_config_yaml = get_current_yaml(file_path)
            d_diff = DeepDiff(previous_config_yaml, current_config_yaml, ignore_order=False)
            print(d_diff)


def get_current_yaml(file_path):
    with open(file_path, "r") as stream:
        try:
            current_yaml = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return current_yaml;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_fun('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
