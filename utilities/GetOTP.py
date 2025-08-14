

class GetOTP:
    @staticmethod
    def get_otp(context, mobile, tenant_id):
        context.playwright = context.playwright.request.new_context(base_url="http://user-registration-sbox.internal.los.payufin.io")

        headers = {
            'Content-Type': 'application/json'
        }
        query_params = {
            "mobile": mobile,
            "tenantId": tenant_id
        }

        response = context.playwright.get("/v0/user/fetchOtp", params=query_params, headers=headers)

        assert response.status == 200
        otp = response.json()["otpValue"]
        print(f"OTP value is: {otp}")
        return otp
