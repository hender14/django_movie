from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from .models import Category

class LoggedInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""

        # テストユーザーのパスワード
        self.password = 'pass'

        # 各インスタンスメソッドで使うテスト用ユーザーを生成し
        # インスタンス変数に格納しておく
        self.test_user = get_user_model().objects.create_user(
            username='testuser',
            email='work_cup_nakano@yahoo.co.jp',
            password=self.password)

        # テスト用ユーザーでログインする
        self.client.login(email=self.test_user.email, password=self.password)


class TestCategoryCreateView(LoggedInTestCase):
    """CategoryCreateView用のテストクラス"""

    def test_create_category_success(self):
        """動画アップロード処理が成功することを検証する"""

        # Postパラメータ
        params = {'name': 'テストタイトル',
                'description': 'テスト項目1',
                'original_name': 'テスト項目2',
                'filename': 'テスト項目3',
                'author': 'username'}

        # 新規動画アップロード処理(Post)を実行
        response = self.client.post(reverse_lazy('lunchmap:create'), params)

        # # 動画一覧ページへのリダイレクトを検証
        # self.assertRedirects(response, reverse_lazy('lunchmap:index'))

        # 動画データがDBに登録されたかを検証
        self.assertEqual(Category.objects.filter(name='テストタイトル').count(), 1)

    def test_create_category_failure(self):
        """新規動画アップロード処理が失敗することを検証する"""

        # 新規動画アップロード処理(Post)を実行
        response = self.client.post(reverse_lazy('lunchmap:create'))

        # 必須フォームフィールドが未入力によりエラーになることを検証
        self.assertFormError(response, 'form', 'name', 'This field is required.')


class TestCategoryUpdateView(LoggedInTestCase):
    """CategoryUpdateView用のテストクラス"""

    def test_update_category_success(self):
        """動画編集処理が成功することを検証する"""

        # テスト用動画データの作成
        # category = Category.objects.create(author=self.test_user, name='タイトル編集前')
        category = Category.objects.create(name='タイトル編集前')
        # Postパラメータ
        params = {'name': 'タイトル編集後'}

        # 動画編集処理(Post)を実行
        response = self.client.post(reverse_lazy('lunchmap:update', kwargs={'pk': category.pk}), params)

        # # 動画詳細ページへのリダイレクトを検証
        # self.assertRedirects(response, reverse_lazy('lunchmap:detail', kwargs={'pk': category.pk}))

        # 動画データが編集されたかを検証
        self.assertEqual(Category.objects.get(pk=category.pk).name, 'タイトル編集後')

    def test_update_category_failure(self):
        """動画編集処理が失敗することを検証する"""

        # 動画編集処理(Post)を実行
        response = self.client.post(reverse_lazy('lunchmap:update', kwargs={'pk': 999}))

        # 存在しない動画データを編集しようとしてエラーになることを検証
        self.assertEqual(response.status_code, 404)


class TestCategoryDeleteView(LoggedInTestCase):
    """CategoryDeleteView用のテストクラス"""

    def test_delete_category_success(self):
        """動画削除処理が成功することを検証する"""

        # テスト用動画データの作成
        # category = Category.objects.create(author=self.test_user, name='タイトル')
        category = Category.objects.create(name='タイトル')

        # 動画削除処理(Post)を実行
        response = self.client.post(reverse_lazy('lunchmap:delete', kwargs={'pk': category.pk}))

        # 動画リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('lunchmap:index'))

        # 動画データが削除されたかを検証
        self.assertEqual(Category.objects.filter(pk=category.pk).count(), 0)

    def test_delete_diary_failure(self):
        """動画削除処理が失敗することを検証する"""

        # 動画削除処理(Post)を実行
        response = self.client.post(reverse_lazy('lunchmap:delete', kwargs={'pk': 999}))

        # 存在しない動画データを削除しようとしてエラーになることを検証
        self.assertEqual(response.status_code, 404)
