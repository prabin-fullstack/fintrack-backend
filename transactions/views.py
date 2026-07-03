from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializer import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from datetime import timedelta
from django.utils import timezone
from collections import defaultdict
# Create your views here.



class TrasactionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        transactions = Transaction.objects.filter(user=request.user)
        serializer = TransactionSerializer(transactions, many=True)

        total_income = (
            Transaction.objects
            .filter(user=request.user, transaction_type='income')
            .aggregate(total=Sum('amount'))['total'] or 0
        )

        total_expense = (
            Transaction.objects
            .filter(user=request.user, transaction_type='expense')
            .aggregate(total=Sum('amount'))['total'] or 0
        )

        balance = total_income - total_expense

        weekly_data = defaultdict(lambda: {"income": 0, "expense": 0})

        for transaction in transactions:
            day = transaction.date.strftime("%a").upper()

            if transaction.transaction_type == "income":
                weekly_data[day]["income"] += float(transaction.amount)
            else:
                weekly_data[day]["expense"] += float(transaction.amount)

        chart_data = []

        for day in ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]:
            chart_data.append({
                "day": day,
                "income": weekly_data[day]["income"],
                "expense": weekly_data[day]["expense"]
            })
        
        print(chart_data)

        return Response({
            "transactions": serializer.data,
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
            "weekly_data": chart_data,
        })


    
    
    
class AddTransactionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)  # Save logged-in user

            return Response(
                {"message": "Transaction added successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DeleteTransactionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        transaction = get_object_or_404(
            Transaction,
            id=id,
            user=request.user
        )

        transaction.delete()

        return Response(
            {"message": "Transaction deleted successfully"},
            status=status.HTTP_200_OK
        )
    

class UpdateTransactionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        transaction = get_object_or_404(
            Transaction,
            id=id,
            user=request.user
        )

        serializer = TransactionSerializer(
            transaction,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class SingleTransactionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        transaction = get_object_or_404(
            Transaction,
            id=id,
            user=request.user
        )

        serializer = TransactionSerializer(transaction)

        return Response(serializer.data)