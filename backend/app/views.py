from flask_restful import Api, Resource
from .models import *
from flask_restful import reqparse
import json

# api instance
api = Api(app)


class BusinessStatistic(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'business_type', type=str, required=True, choices=['Savings', 'Loan'],
        help="business_type must in ['Savings', 'Loan']"
    )
    parser.add_argument(
        'time_step', type=str, required=True, choices=['Day', 'Month', 'Year'],
        help="time_step must in ['Day', 'Month', 'Year']"
    )
    parser.add_argument('start_time', type=str, required=True, help="Must contain start_time")
    parser.add_argument('end_time', type=str, required=True, help="Must contain end_time")

    def post(self):
        args = self.parser.parse_args()
        banks = [item.sb_name for item in SubBank.query.all()]
        result = {
            'success': 1,
            'business_type': args['business_type'],
            'start_time': args['start_time'],
            'end_time': args['end_time'],
            'data': []
        }
        for b in banks:
            users = 0
            money = 0
            if args['business_type'] == 'Savings':
                accounts = SavingsAccountRecord.query.filter(
                    SavingsAccountRecord.sar_sb_name == b
                )
                a_id = [x.sar_a_code for x in accounts]
                for id in a_id:
                    tmp = Account.query.filter(
                        Account.a_code == id
                    ).filter(
                        Account.a_open_date >= args["start_time"]
                    ).filter(
                        Account.a_open_date < args["end_time"]
                    ).first()
                    if tmp is None:
                        continue
                    users = users + 1
                    money = money + tmp.a_balance
            else:
                loans = Loan.query.filter(
                    Loan.l_sb_name == b
                )
                for l in loans:
                    tmp = LoanPayment.query.filter(
                        LoanPayment.lp_l_code == l.l_code
                    ).filter(
                        LoanPayment.lp_date >= args["start_time"]
                    ).filter(
                        LoanPayment.lp_date < args["end_time"]
                    )
                    if tmp is None:
                        continue
                    for t in tmp:
                        money = money + t.lp_money
                    users = users + len(LoanCustomer.query.filter(
                        LoanCustomer.lc_l_code == l.l_code
                    ))
            result["data"].append({
                'bank_name': b,
                'users': users,
                'money': money
            })
        return result, 200



api.add_resource(
    BusinessStatistic, '/api/business-statistic'
)
