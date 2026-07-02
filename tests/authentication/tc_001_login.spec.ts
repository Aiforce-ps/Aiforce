import { test, expect } from '@playwright/test';

// ASSUMPTION: base URL provided in configuration
const BASE_URL = 'https://example.com';

test.describe('TC-001: Successful Login with Valid Credentials and T&C Accepted', () => {
  
test('User should be able to login successfully', async ({ page }) => {
    // Step 1: Navigate to the login page
    await page.goto(`${BASE_URL}/login`);
    await page.waitForLoadState('networkidle');
    await expect(page.getByRole('textbox', { name: /username/i })).toBeVisible();
    await expect(page.getByLabel('Password')).toBeVisible();
    await expect(page.getByRole('checkbox', { name: /terms & conditions/i })).toBeVisible();
    await expect(page.getByRole('button', { name: /sign in/i })).toBeVisible();

    // Step 2: Enter username
    await page.fill(page.getByRole('textbox', { name: /username/i }), 'testuser01');
    await expect(page.getByRole('textbox', { name: /username/i })).toHaveValue('testuser01');

    // Step 3: Enter password
    await page.fill(page.getByLabel('Password'), 'Test@1234');
    await expect(page.getByLabel('Password')).toHaveAttribute('type', 'password');

    // Step 4: Check the Terms & Conditions checkbox
    await page.check(page.getByRole('checkbox', { name: /terms & conditions/i }));
    await expect(page.getByRole('checkbox', { name: /terms & conditions/i })).toBeChecked();

    // Step 5: Click the Sign In button
    await page.click(page.getByRole('button', { name: /sign in/i }));
    await page.waitForLoadState('networkidle');
    await expect(page).toHaveURL(/dashboard/); // Assuming the dashboard URL contains 'dashboard'

    // Expected Result: User successfully logs in and lands on the dashboard
    // No error messages displayed
  });
});
