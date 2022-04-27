from flask import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL #pip install flask-mysql
import pymysql
  
app = Flask(__name__)

@app.route('/messages')
def messages():
    try:
        conn = MySQLConnection.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from messages")
        postslist = cursor.fetchall()
        user_id = 5
        postArray = []
        for row in postslist:
            post_id = row['id']
            type = -1
            #print(message_id)
            cursor.execute("SELECT count(*) as cntStatus,type FROM like_unlike WHERE user_id=%s AND post_id=%s", (user_id, post_id))
            rs1 = cursor.fetchone()
            count_status = rs1['cntStatus']
            #print(count_status)
            if count_status > 0:
                type = rs1['type']

            cursor.execute("SELECT COUNT(*) AS cntLikes FROM like_unlike WHERE type=1 and post_id=%s", post_id)
            rs2 = cursor.fetchone()
            total_likes = rs2['cntLikes']
            #print(total_likes)

            cursor.execute("SELECT COUNT(*) AS cntUnlikes FROM like_unlike WHERE type=0 and post_id=%s", post_id)
            rs3 = cursor.fetchone()
            total_unlikes = rs3['cntUnlikes']
            #print(total_unlikes)

            if type == 1:
                txtcolor = 'color: #ffa449;' 
            else:
                txtcolor = ''  

            if type == 0:
                txtcolor2 = 'color: #ffa449;' 
            else:
                txtcolor2 = ''

            postObj = {
                    'id': row['id'],
                    'message': row['message'],
                    'total_likes': total_likes,
                    'total_unlikes': total_unlikes,
                    'txtcolor': txtcolor,
                    'txtcolor2': txtcolor2}
            postArray.append(postObj)
        return render_template('messages.html',postall=postArray)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route("/likeunlike",methods=["POST","GET"])
def likeunlike():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if request.method == 'POST':
            user_id = 7
            post_id = request.form['post_id'] 
            type = request.form['type']
            #print(post_id)
            #print(type)
            cursor.execute("SELECT COUNT(*) AS cntpost FROM like_unlike WHERE post_id=%s AND user_id=%s", (post_id, user_id))
            rscount = cursor.fetchone()
            count = rscount['cntpost']
            #print(count)

            if count == 0:
                sql = "INSERT INTO like_unlike(user_id,post_id,type) VALUES(%s, %s, %s)"
                data = (user_id, post_id, type)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()

                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("SELECT COUNT(*) AS cntLike FROM like_unlike WHERE type=1 AND post_id=%s",post_id)
                rscounttotal = cur.fetchone()
                countlike = rscounttotal['cntLike']
                #print(countlike)

                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("SELECT COUNT(*) AS cntUnlike FROM like_unlike WHERE type=0 AND post_id=%s",post_id)
                rscounttotalunlike = cur.fetchone()
                countUnlike = rscounttotalunlike['cntUnlike']
                #print(countUnlike)

                totallikeajax = countlike
                totalunlikeajax = countUnlike
            else:
                sql = "UPDATE like_unlike SET type=%s WHERE user_id=%s AND post_id=%s"
                data = (type, user_id, post_id)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()

                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("SELECT COUNT(*) AS cntLike FROM like_unlike WHERE type=1 AND post_id=%s",post_id)
                rscounttotal = cur.fetchone()
                countlike = rscounttotal['cntLike']
                #print(countlike)

                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("SELECT COUNT(*) AS cntUnlike FROM like_unlike WHERE type=0 AND post_id=%s",post_id)
                rscounttotalunlike = cur.fetchone()
                countUnlike = rscounttotalunlike['cntUnlike']
                #print(countUnlike)
                
                totallikeajax = countlike
                totalunlikeajax = countUnlike
        return jsonify({"likes":totallikeajax,"unlikes":totalunlikeajax})
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()