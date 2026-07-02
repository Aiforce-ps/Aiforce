import { test, expect } from '@playwright/test';

// ASSUMPTION: base URL defaulted — replace before execution
const baseURL = 'https://example.com';

test.describe('TC-001: Successful Login with Valid Credentials and T&C Accepted', () => {
  test('User successfully logs in and lands on the dashboard', async ({ page }) => {
    // Step 1: Navigate to the login page
    await page.goto(`${baseURL}/login`);
    await page.waitForLoadState('networkidle');
    await expect(page.getByRole('textbox', { name: /username/i })).toBeVisible();
    await expect(page.getByLabel('Password')).toBeVisible();
    await expect(page.getByRole('checkbox', { name: /terms & conditions/i })).toBeVisible();
    await expect(page.getByRole('button', { name: /sign in/i })).toBeVisible();

    // Step 2: Enter username
    await page.getByRole('textbox', { name: /username/i }).fill('testuser01');
    await expect(page.getByRole('textbox', { name: /username/i })).toHaveValue('testuser01');

    // Step 3: Enter password
    await page.getByLabel('Password').fill('Test@1234');
    await expect(page.getByLabel('Password')).toHaveAttribute('type', 'password');

    // Step 4: Check the Terms & Conditions checkbox
    await page.getByRole('checkbox', { name: /terms & conditions/i }).check();
    await expect(page.getByRole('checkbox', { name: /terms & conditions/i })).toBeChecked();

    // Step 5: Click the Sign In button
    await page.getByRole('button', { name: /sign in/i }).click();
    await page.waitForLoadState('networkidle');
    await expect(page).toHaveURL(/dashboard/);

    // Expected Result: User successfully logs in and lands on the dashboard
    // No error messages displayed
    // (Assuming there's no specific locator for error messages to check)
  });
});
