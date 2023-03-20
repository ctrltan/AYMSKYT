from django.test import TestCase
from django.urls import reverse
from minted.models import RewardClaim, Reward, User


class ClaimRewardViewTestCase(TestCase):
    """Unit tests for the Rewards Homepage view"""

    fixtures = [
        'minted/tests/fixtures/default_user.json',
        'minted/tests/fixtures/default_other_user.json',
        'minted/tests/fixtures/default_spending_limit.json',
        'minted/tests/fixtures/default_rewards.json',
        'minted/tests/fixtures/default_reward_claims.json'
    ]

    def setUp(self):
        self.reward = Reward.objects.get(pk=1)
        self.url = reverse('claim_reward', kwargs={ 'brand_name': self.reward.brand_name, 'reward_id': self.reward.reward_id })
        self.user = User.objects.get(pk=1)
        self.claim = RewardClaim.objects.get(pk=1)
        self.other_user = User.objects.get(pk=2)

    def test_claim_reward_url(self):
        self.assertEqual(self.url, f'/rewards/{self.reward.brand_name}/{self.reward.reward_id}/')

    def test_get_claim_rewards(self):
        self.client.login(email=self.user.email, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rewards/rewards_claim.html')

    def test_get_claim_reward_redirects_on_invalid_reward_id(self):
        self.client.login(email=self.user.email, password='Password123')
        redirect_url = reverse('rewards')
        self.url = reverse('claim_reward', kwargs={ 'brand_name': self.reward.brand_name, 'reward_id': 'APP010' })

        response = self.client.get(self.url, follow=True)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)
    
    def test_get_claim_reward_redirects_if_user_does_not_have_reward(self):
        self.client.login(email=self.user.email, password='Password123')
        redirect_url = reverse('rewards')
        self.reward = Reward.objects.get(pk=3)
        self.url = reverse('claim_reward', kwargs={ 'brand_name': self.reward.brand_name, 'reward_id': self.reward.reward_id })

        response = self.client.get(self.url, follow=True)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)
    
    def test_get_claim_reward_redirects_if_user_does_not_have_enough_points(self):
        self.client.login(email = self.other_user.email, password = 'Password123')
        redirect_url = reverse('rewards')
        self.url = reverse('claim_reward', kwargs={ 'brand_name': self.reward.brand_name, 'reward_id': self.reward.reward_id  })

        response = self.client.get(self.url, follow=True)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)