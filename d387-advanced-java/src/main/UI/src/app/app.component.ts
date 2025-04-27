import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  constructor(private httpClient: HttpClient) {}

  private baseURL: string = 'http://localhost:8080';
  private getUrl: string = this.baseURL + '/room/reservation/v1/';
  private postUrl: string = this.baseURL + '/room/reservation/v1';

  public submitted!: boolean;
  public roomsearch!: FormGroup;
  public rooms!: Room[];
  public request!: ReserveRoomRequest;
  public currentCheckInVal!: string;
  public currentCheckOutVal!: string;

  public englishWelcomeMessage$!: Observable<string>;
  public frenchWelcomeMessage$!: Observable<string>;
  public presentationTimes!: { [key: string]: string }; // Holds ET, MT, UTC

  ngOnInit(): void {
    this.roomsearch = new FormGroup({
      checkin: new FormControl(''),
      checkout: new FormControl('')
    });

    this.englishWelcomeMessage$ = this.httpClient.get(this.baseURL + '/welcome?lang=en-US', { responseType: 'text' });
    this.frenchWelcomeMessage$ = this.httpClient.get(this.baseURL + '/welcome?lang=fr-CA', { responseType: 'text' });

    this.httpClient.get<{ [key: string]: string }>(`${this.baseURL}/presentation`)
      .subscribe(data => this.presentationTimes = data);

    this.roomsearch.valueChanges.subscribe(x => {
      this.currentCheckInVal = x.checkin;
      this.currentCheckOutVal = x.checkout;
    });
  }

  onSubmit({ value, valid }: { value: Roomsearch, valid: boolean }): void {
    this.getAll().subscribe(rooms => {
      this.rooms = <Room[]>Object.values(rooms)[0];
      this.rooms.forEach(room => {
        room.priceCad = (Number(room.price) * 1.35).toFixed(2);
        room.priceEur = (Number(room.price) * 0.92).toFixed(2);
      });
    });
  }

  reserveRoom(value: string): void {
    this.request = new ReserveRoomRequest(value, this.currentCheckInVal, this.currentCheckOutVal);
    this.createReservation(this.request);
  }

  createReservation(body: ReserveRoomRequest): void {
    const options = {
      headers: new HttpHeaders().append('key', 'value'),
    };

    this.httpClient.post(this.postUrl, body, options)
      .subscribe(res => console.log(res));
  }

  getAll(): Observable<any> {
    return this.httpClient.get(
      `${this.baseURL}/room/reservation/v1?checkin=${this.currentCheckInVal}&checkout=${this.currentCheckOutVal}`,
      { responseType: 'json' }
    );
  }
}

export interface Roomsearch {
  checkin: string;
  checkout: string;
}

export interface Room {
  id: string;
  roomNumber: string;
  price: string;
  priceCad?: string;
  priceEur?: string;
  links: string;
}

export class ReserveRoomRequest {
  roomId: string;
  checkin: string;
  checkout: string;

  constructor(roomId: string, checkin: string, checkout: string) {
    this.roomId = roomId;
    this.checkin = checkin;
    this.checkout = checkout;
  }
}
